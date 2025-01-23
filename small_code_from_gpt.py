
import toga
from toga.style import Pack
from toga.constants import COLUMN

#        "appId": "ca-app-pub-3940256099942544~3347511713",
#        "banId": "ca-app-pub-3940256099942544/6300978111",
#        "intId": "ca-app-pub-3940256099942544/1033173712",


class AdMobApp(toga.App):
    def startup(self):
        # Create the main window
        self.main_window = toga.MainWindow(title="AdMob Example")

        # Create a Toga Box widget for layout
        self.box = toga.Box(style=Pack(direction=COLUMN, padding=10))

        # Add a button to trigger an interstitial ad (optional)
        show_ad_button = toga.Button(
            "Show Interstitial Ad", on_press=self.show_interstitial_ad, style=Pack(padding=10)
        )
        self.box.add(show_ad_button)

        # Add the layout to the main window
        self.main_window.content = self.box
        self.main_window.show()

        self.setup_admob()

    def setup_admob(self):
        # Access the native Android RelativeLayout
        native_layout = self.box._impl.native
        if toga.platform == "android":
            from java import jclass

            # Import Java classes
            AdSize = jclass("com.google.android.gms.ads.AdSize")
            AdView = jclass("com.google.android.gms.ads.AdView")
            AdRequest = jclass("com.google.android.gms.ads.AdRequest")
            RelativeLayout = jclass("android.widget.RelativeLayout")
            RelativeLayoutParams = jclass("android.widget.RelativeLayout$LayoutParams")

            # Create an AdView
            ad_view = AdView(native_layout.getContext())
            ad_view.setAdSize(AdSize.BANNER)
            ad_view.setAdUnitId("ca-app-pub-3940256099942544~3347511713")  # Replace with your actual Ad Unit ID

            # Create AdRequest
            ad_request = AdRequest.Builder().build()

            # Request an Ad
            ad_view.loadAd(ad_request)

            # Configure Layout Parameters for the AdView
            layout_params = RelativeLayoutParams(
                RelativeLayoutParams.MATCH_PARENT,
                RelativeLayoutParams.WRAP_CONTENT,
            )
            layout_params.addRule(RelativeLayout.ALIGN_PARENT_BOTTOM)  # Place the ad at the bottom

            # Add the AdView to the native layout
            native_layout.addView(ad_view, layout_params)

    def show_interstitial_ad(self, widget):

        if toga.platform == "android":
            from java import jclass

            # Import Java classes
            InterstitialAd = jclass("com.google.android.gms.ads.InterstitialAd")
            AdRequest = jclass("com.google.android.gms.ads.AdRequest")

            # Create and load the interstitial ad
            activity = jclass("org.kivy.android.PythonActivity").mActivity
            self.interstitial_ad = InterstitialAd(activity)
            self.interstitial_ad.setAdUnitId("ca-app-pub-3940256099942544/1033173712")
            ad_request = AdRequest.Builder().build()
            self.interstitial_ad.loadAd(ad_request)

            # Show the ad if loaded
            if self.interstitial_ad.isLoaded():
                self.interstitial_ad.show()
            else:
                print("Ad not loaded yet.")

def main():
    return AdMobApp("AdMob Integration", "org.beeware.admob")
