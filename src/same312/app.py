import toga
from toga.style import Pack
from toga.constants import CENTER
from toga.constants import COLUMN


test = {
        "appId": "ca-app-pub-3940256099942544~3347511713",
        "banId": "ca-app-pub-3940256099942544/6300978111",
        "intId": "ca-app-pub-3940256099942544/1033173712",
        "testD": []
        }

def main():
    class AdMobApp(toga.App):
        def startup(self):
            self.main_window = toga.MainWindow(self.name)
            layout = toga.Box()    

            box = toga.Box(style=Pack(direction=COLUMN, padding=10))
            # Add a button to trigger an interstitial ad
            show_ad_button = toga.Button(
                "Show Interstitial Ad", on_press=self.show_interstitial_ad, style=Pack(padding=10)
            )
            box.add(show_ad_button)

            # Add the layout to the main window
            self.main_window.content = box
            self.main_window.show()

            # Initialize AdMob only on Android
            if toga.platform == "android":
                #self.initialize_admob()
                self.setup_admob()

            if toga.platform == "android":
                from java import jclass
                AdListener = jclass("com.google.android.gms.ads.AdListener")
                AdMobAdapter = jclass("com.google.ads.mediation.admob.AdMobAdapter")
                AdRequest = jclass("com.google.android.gms.ads.AdRequest")
                AdRequestBuilder = jclass("com.google.android.gms.ads.AdRequest$Builder")
                AdSize = jclass("com.google.android.gms.ads.AdSize")
                AdView = jclass("com.google.android.gms.ads.AdView")
                Bundle = jclass("android.os.Bundle")
                Gravity = jclass("android.view.Gravity")
                InterstitialAd = jclass("com.google.android.gms.ads.InterstitialAd")
                LayoutParams = jclass("android.view.ViewGroup$LayoutParams")
                LinearLayout = jclass("android.widget.LinearLayout")
                View = jclass("android.view.View")
                Color = jclass('android.graphics.Color')
                MobileAds = jclass("com.google.android.gms.ads.MobileAds")
                activity = jclass("org.kivy.android.PythonActivity")


                class Admob(toga.App):
                    def __init__(self, Window,adId=test):
                        self.ad = adId
                        self.Window=Window
                        self.ad_size = 0
                        self._loaded = False
                        self.visiable = False
                        self._test_devices = self.ad["testD"] if "testD" in self.ad.keys() and isinstance(self.ad["testD"], list) else []
                        MobileAds.initialize(activity, self.ad["appId"])

                    # Banner Ad
                    def new_banner(self,position = None, color = None, margin = 0):
                        self._adview = AdView(activity)
                        adsize = AdSize.getCurrentOrientationAnchoredAdaptiveBannerAdSize(activity, self.Window.width - margin)
                        self.ad_size = adsize.getHeight()
                        self._adview.setAdSize(adsize)
                        self._adview.setAdUnitId(self.ad["banId"])
                        self._adview.setVisibility(View.GONE)
                        if color:
                            self._adview.setBackgroundColor(Color.parseColor(str(color)))
                        else:
                            self._adview.setBackgroundColor(Color.TRANSPARENT)
                        adLayoutParams = LayoutParams(
                            LayoutParams.MATCH_PARENT, LayoutParams.WRAP_CONTENT
                        )

                        self._adview.setLayoutParams(adLayoutParams)
                        layout = LinearLayout(activity)
                            
                        if isinstance(position, list)  or isinstance(position, tuple):
                            self._adview.setX(position[0])
                            self._adview.setY(position[1])
                        elif isinstance(position,int):
                            self._adview.setY(position)
                            self._adview.setX(0)
                        elif isinstance(position, str):
                            if position == "bottom":
                                layout.setGravity(Gravity.BOTTOM)

                        layout.addView(self._adview)
                        layoutParams = LayoutParams(
                            LayoutParams.MATCH_PARENT, LayoutParams.MATCH_PARENT
                        )
                        layout.setLayoutParams(layoutParams)       
                        activity.addContentView(layout, layoutParams)        

                    def request_banner(self, options={}):
                        self._adview.loadAd(self._get_builder(options).build())
                        print('KivMobLite: new_banner called')
                        
                    def show_banner(self):
                        self._adview.setVisibility(View.VISIBLE)
                        self.visiable = True
                        print('KivMobLite: show_banner called')


                    def hide_banner(self):
                        self._adview.setVisibility(View.GONE)
                        self.visible = False
                        print('KivMobLite: hide_banner called')

                    def destroy_banner(self):
                        self._adview.destroy()
                        self.visible = False
                        print('KivMobLite: destroy_banner called')
                            
                    def banner_pos(self, position = None):
                        self.hide_banner()
                        if isinstance(position, list)  or isinstance(position, tuple):
                            self._adview.setX(position[0])
                            self._adview.setY(position[1])
                        elif isinstance(position, int) or isinstance(position, float):
                            self._adview.setX(0)
                            self._adview.setY(position)
                        elif isinstance(position, str):
                            if position == "top":
                                self._adview.setX(0)
                                self._adview.setY(0)
                            else:
                                bottom = self.Window.height - self.ad_size
                                self._adview.setX(0)
                                self._adview.setY(bottom)
                        self.show_banner()

                    #@run_on_ui_thread
                    def new_interstitial(self):
                #        self._interstitial = InterstitialAd(self.activity.mActivity)
                        self._interstitial = InterstitialAd(self.activity)

                        self._interstitial.setAdUnitId(self.ad["intId"])
                        
                    #@run_on_ui_thread
                    def request_interstitial(self, options={}):
                        self._interstitial.loadAd(self._get_builder(options).build())
                        print('KivMobLite: new_interstitial called')

                    #@run_on_ui_thread
                    def _is_interstitial_loaded(self):
                        self._loaded = self._interstitial.isLoaded()

                    def is_interstitial_loaded(self):
                        self._is_interstitial_loaded()
                        return self._loaded

                    #@run_on_ui_thread
                    def show_interstitial(self):
                        if self.is_interstitial_loaded():
                            self._interstitial.show()
                            
                    #@run_on_ui_thread
                    def destroy_interstitial(self):
                        self._interstitial.destroy()

                    def _get_builder(self, options):
                        builder = AdRequestBuilder()
                        if options is not None:
                            if "children" in options:
                                builder.tagForChildDirectedTreatment(options["children"])
                            if "family" in options:
                                extras = Bundle()
                                extras.putBoolean(
                                    "is_designed_for_families", options["family"]
                                )
                                builder.addNetworkExtrasBundle(AdMobAdapter, extras)
                        if self._test_devices:
                            for test_device in self._test_devices:
                                builder.addTestDevice(test_device)
                        return builder

                       
                #CODES THAT ARE NOT SEEN BY THE COMPILER?
                ads = Admob(self.main_window,test)
                ads.new_banner(position = "bottom", color = "#ffffff", margin = 0) # Adaptive banner
                ads.request_banner()
                ads.show_banner()

                layout.add(ads)

                self.main_window.content = layout
                self.main_window.show()


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
                ad_view.setAdUnitId("YOUR_AD_UNIT_ID")  # Replace with your actual Ad Unit ID

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









        def initialize_admob(self):

            if toga.platform == "android":

                # Java classes for AdMob
                from java import jclass

                MobileAds = jclass("com.google.android.gms.ads.MobileAds")
                AdView = jclass("com.google.android.gms.ads.AdView")
                AdRequestBuilder = jclass("com.google.android.gms.ads.AdRequest$Builder")
                AdSize = jclass("com.google.android.gms.ads.AdSize")
                LinearLayout = jclass("android.widget.LinearLayout")
                LayoutParams = jclass("android.widget.LinearLayout$LayoutParams")
                View = jclass("android.view.View")
                activity = jclass("org.kivy.android.PythonActivity").mActivity

                # Initialize MobileAds SDK
                MobileAds.initialize(activity)

                # Create a banner ad
                self.ad_view = AdView(activity)
                self.ad_view.setAdSize(AdSize.BANNER)
                self.ad_view.setAdUnitId("ca-app-pub-3940256099942544/6300978111")

                # Load the banner ad
                ad_request = AdRequestBuilder().build()
                self.ad_view.loadAd(ad_request)

                # Create a layout to host the ad
                ad_layout = LinearLayout(activity)
                ad_layout.setOrientation(LinearLayout.VERTICAL)
                ad_layout.addView(self.ad_view, LayoutParams(LayoutParams.MATCH_PARENT, LayoutParams.WRAP_CONTENT))

                # Attach the ad layout to the app's activity
                activity.addContentView(ad_layout, LayoutParams(LayoutParams.MATCH_PARENT, LayoutParams.MATCH_PARENT))

        def show_interstitial_ad(self, widget):
            if toga.platform == "android":

                from java import jclass

                # Java classes for Interstitial Ads
                InterstitialAd = jclass("com.google.android.gms.ads.InterstitialAd")
                AdRequestBuilder = jclass("com.google.android.gms.ads.AdRequest$Builder")
                activity = jclass("org.kivy.android.PythonActivity").mActivity

                # Create an interstitial ad
                self.interstitial_ad = InterstitialAd(activity)
                self.interstitial_ad.setAdUnitId("ca-app-pub-3940256099942544/1033173712")

                # Load the ad
                ad_request = AdRequestBuilder().build()
                self.interstitial_ad.loadAd(ad_request)

                # Show the ad when loaded
                if self.interstitial_ad.isLoaded():
                    self.interstitial_ad.show()
                else:
                    print("Ad not loaded yet.")


    return AdMobApp('AdMob App', 'org.beeware.admob')
    


























