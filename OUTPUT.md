
```

Select device:

  1) @beePhone (emulator)
  2) Create a new Android emulator

> 1

In future, you can specify this device by running:

    $ briefcase run android -d "@beePhone"

[same312] Starting emulator beePhone...
Starting emulator... done

[same312] Starting app on @beePhone (running emulator) (device ID emulator-5554)

[same312] Installing app...
Stopping old versions of the app... done
Installing new app version... done
Launching app... done

[same312] Following device log output (type CTRL-C to stop log)...
===========================================================================
--------- beginning of main
I/example.same31: Late-enabling -Xcheck:jni
W/example.same31: Unexpected CPU variant for X86 using defaults: x86_64
D/CompatibilityChangeReporter: Compat change id reported: 171979766; UID 10107; state: ENABLED
V/GraphicsEnvironment: ANGLE Developer option for 'com.example.same312' set to: 'default'
V/GraphicsEnvironment: Neither updatable production driver nor prerelease driver is supported.
D/NetworkSecurityConfig: Using Network Security Config from resource network_security_config debugBuild: true
D/NetworkSecurityConfig: Using Network Security Config from resource network_security_config debugBuild: true
D/AppCompatDelegate: Checking for metadata for AppLocalesMetadataHolderService : Service not found
D/MainActivity: onCreate() start
D/libEGL  : loaded /vendor/lib64/egl/libEGL_emulation.so
D/libEGL  : loaded /vendor/lib64/egl/libGLESv1_CM_emulation.so
D/libEGL  : loaded /vendor/lib64/egl/libGLESv2_emulation.so
W/example.same31: Accessing hidden method Landroid/view/View;->computeFitSystemWindows(Landroid/graphics/Rect;Landroid/graphics/Rect;)Z (unsupported, reflection, allowed)
W/example.same31: Accessing hidden method Landroid/view/ViewGroup;->makeOptionalFitsSystemWindows()V (unsupported, reflection, allowed)
D/MainActivity: Starting Python
W/native.stderr: Could not find platform independent libraries <prefix>
W/native.stderr: Could not find platform dependent libraries <exec_prefix>
W/native.stderr: Consider setting $PYTHONHOME to <prefix>[:<exec_prefix>]
W/example.same312: type=1400 audit(0.0:452): avc: granted { execute } for path="/data/data/com.example.same312/files/chaquopy/bootstrap-native/x86_64/zlib.so" dev="dm-5" ino=123536 scontext=u:r:untrusted_app:s0:c107,c256,c512,c768 tcontext=u:object_r:app_data_file:s0:c107,c256,c512,c768 tclass=file app=com.example.same312
W/example.same312: type=1400 audit(0.0:453): avc: granted { execute } for path="/data/data/com.example.same312/files/chaquopy/bootstrap-native/x86_64/java/chaquopy.so" dev="dm-5" ino=123525 scontext=u:r:untrusted_app:s0:c107,c256,c512,c768 tcontext=u:object_r:app_data_file:s0:c107,c256,c512,c768 tclass=file app=com.example.same312
W/example.same312: type=1400 audit(0.0:454): avc: granted { execute } for path="/data/data/com.example.same312/files/chaquopy/bootstrap-native/x86_64/_ctypes.so" dev="dm-5" ino=123529 scontext=u:r:untrusted_app:s0:c107,c256,c512,c768 tcontext=u:object_r:app_data_file:s0:c107,c256,c512,c768 tclass=file app=com.example.same312
W/example.same312: type=1400 audit(0.0:455): avc: granted { execute } for path="/data/data/com.example.same312/files/chaquopy/bootstrap-native/x86_64/_struct.so" dev="dm-5" ino=123522 scontext=u:r:untrusted_app:s0:c107,c256,c512,c768 tcontext=u:object_r:app_data_file:s0:c107,c256,c512,c768 tclass=file app=com.example.same312
W/example.same312: type=1400 audit(0.0:456): avc: granted { execute } for path="/data/data/com.example.same312/files/chaquopy/bootstrap-native/x86_64/_bz2.so" dev="dm-5" ino=123531 scontext=u:r:untrusted_app:s0:c107,c256,c512,c768 tcontext=u:object_r:app_data_file:s0:c107,c256,c512,c768 tclass=file app=com.example.same312
W/example.same312: type=1400 audit(0.0:457): avc: granted { execute } for path="/data/data/com.example.same312/files/chaquopy/bootstrap-native/x86_64/_lzma.so" dev="dm-5" ino=123532 scontext=u:r:untrusted_app:s0:c107,c256,c512,c768 tcontext=u:object_r:app_data_file:s0:c107,c256,c512,c768 tclass=file app=com.example.same312
W/example.same312: type=1400 audit(0.0:458): avc: granted { execute } for path="/data/data/com.example.same312/files/chaquopy/bootstrap-native/x86_64/math.so" dev="dm-5" ino=123527 scontext=u:r:untrusted_app:s0:c107,c256,c512,c768 tcontext=u:object_r:app_data_file:s0:c107,c256,c512,c768 tclass=file app=com.example.same312
W/example.same312: type=1400 audit(0.0:459): avc: granted { execute } for path="/data/data/com.example.same312/files/chaquopy/bootstrap-native/x86_64/_datetime.so" dev="dm-5" ino=123535 scontext=u:r:untrusted_app:s0:c107,c256,c512,c768 tcontext=u:object_r:app_data_file:s0:c107,c256,c512,c768 tclass=file app=com.example.same312
W/asset   : seek out of range: want -20, end=22
D/MainActivity: Running main module same312
I/python.stdout: WARNING: Can't find app icon; falling back to default icon
I/python.stdout: Python app launched & stored in Android Activity class
W/python.stderr: /data/data/com.example.same312/files/chaquopy/AssetFinder/app/same312/app.py:433: DeprecationWarning: App.name is deprecated. Use formal_name instead
I/python.stdout: Toga app: onCreate
D/MainActivity: onCreate() complete
D/MainActivity: onStart() start
I/python.stdout: Toga app: onStart
D/MainActivity: onStart() complete
D/MainActivity: onResume() start
I/python.stdout: Toga app: onResume
D/MainActivity: onResume() complete
D/MainActivity: onTopResumedActivityChanged() start
D/MainActivity: onTopResumedActivityChanged() complete
I/Choreographer: Skipped 107 frames!  The application may be doing too much work on its main thread.
D/HostConnection: createUnique: call
D/HostConnection: HostConnection::get() New Host Connection established 0x769f43e0c590, tid 6279
D/HostConnection: HostComposition ext ANDROID_EMU_CHECKSUM_HELPER_v1 ANDROID_EMU_native_sync_v2 ANDROID_EMU_dma_v1 ANDROID_EMU_direct_mem ANDROID_EMU_host_composition_v1 ANDROID_EMU_host_composition_v2 ANDROID_EMU_vulkan ANDROID_EMU_deferred_vulkan_commands ANDROID_EMU_vulkan_null_optional_strings ANDROID_EMU_vulkan_create_resources_with_requirements ANDROID_EMU_YUV_Cache ANDROID_EMU_vulkan_ignored_handles ANDROID_EMU_has_shared_slots_host_memory_allocator ANDROID_EMU_vulkan_free_memory_sync ANDROID_EMU_vulkan_shader_float16_int8 ANDROID_EMU_vulkan_async_queue_submit ANDROID_EMU_vulkan_queue_submit_with_commands ANDROID_EMU_sync_buffer_data ANDROID_EMU_vulkan_async_qsri ANDROID_EMU_read_color_buffer_dma GL_OES_EGL_image_external_essl3 GL_OES_vertex_array_object GL_KHR_texture_compression_astc_ldr ANDROID_EMU_host_side_tracing ANDROID_EMU_gles_max_version_3_0 
W/OpenGLRenderer: Failed to initialize 101010-2 format, error = EGL_SUCCESS
I/Gralloc4: mapper 4.x is not supported
D/HostConnection: createUnique: call
D/HostConnection: HostConnection::get() New Host Connection established 0x769f43e0d490, tid 6279
D/goldfish-address-space: allocate: Ask for block of size 0x100
D/goldfish-address-space: allocate: ioctl allocate returned offset 0x3ebffe000 size 0x2000
W/Gralloc4: allocator 4.x is not supported
D/HostConnection: HostComposition ext ANDROID_EMU_CHECKSUM_HELPER_v1 ANDROID_EMU_native_sync_v2 ANDROID_EMU_dma_v1 ANDROID_EMU_direct_mem ANDROID_EMU_host_composition_v1 ANDROID_EMU_host_composition_v2 ANDROID_EMU_vulkan ANDROID_EMU_deferred_vulkan_commands ANDROID_EMU_vulkan_null_optional_strings ANDROID_EMU_vulkan_create_resources_with_requirements ANDROID_EMU_YUV_Cache ANDROID_EMU_vulkan_ignored_handles ANDROID_EMU_has_shared_slots_host_memory_allocator ANDROID_EMU_vulkan_free_memory_sync ANDROID_EMU_vulkan_shader_float16_int8 ANDROID_EMU_vulkan_async_queue_submit ANDROID_EMU_vulkan_queue_submit_with_commands ANDROID_EMU_sync_buffer_data ANDROID_EMU_vulkan_async_qsri ANDROID_EMU_read_color_buffer_dma GL_OES_EGL_image_external_essl3 GL_OES_vertex_array_object GL_KHR_texture_compression_astc_ldr ANDROID_EMU_host_side_tracing ANDROID_EMU_gles_max_version_3_0 
W/native.stderr: s_glBindAttribLocation: bind attrib 0 name inPosition
W/native.stderr: s_glBindAttribLocation: bind attrib 1 name inColor
W/native.stderr: s_glBindAttribLocation: bind attrib 2 name inShadowParams
W/native.stderr: s_glBindAttribLocation: bind attrib 0 name inPosition
W/native.stderr: s_glBindAttribLocation: bind attrib 1 name inColor
W/native.stderr: s_glBindAttribLocation: bind attrib 2 name inCircleEdge
W/native.stderr: s_glBindAttribLocation: bind attrib 0 name inPosition
W/native.stderr: s_glBindAttribLocation: bind attrib 1 name inColor
W/native.stderr: s_glBindAttribLocation: bind attrib 2 name inTextureCoords
W/native.stderr: s_glBindAttribLocation: bind attrib 0 name position
W/native.stderr: s_glBindAttribLocation: bind attrib 1 name color
D/MainActivity: onPrepareOptionsMenu() start
D/MainActivity: onPrepareOptionsMenu() complete
I/Choreographer: Skipped 46 frames!  The application may be doing too much work on its main thread.
W/native.stderr: s_glBindAttribLocation: bind attrib 0 name position
W/native.stderr: s_glBindAttribLocation: bind attrib 1 name color
W/native.stderr: s_glBindAttribLocation: bind attrib 2 name localCoord
I/OpenGLRenderer: Davey! duration=2516ms; Flags=1, FrameTimelineVsyncId=3981, IntendedVsync=755299954511, Vsync=757083287773, InputEventId=0, HandleInputStart=757095760562, AnimationStart=757095765140, PerformTraversalsStart=757095980721, DrawStart=757340766726, FrameDeadline=755316621177, FrameInterval=757095612764, FrameStartTime=16666666, SyncQueued=757349349441, SyncStart=757349724648, IssueDrawCommandsStart=757350557806, SwapBuffers=757647776189, FrameCompleted=757816796479, DequeueBufferDuration=5365, QueueBufferDuration=7383422, GpuCompleted=757816796479, SwapBuffersCompleted=757805608845, DisplayPresentTime=1357396445389499248, 
I/OpenGLRenderer: Davey! duration=1250ms; Flags=0, FrameTimelineVsyncId=3987, IntendedVsync=757099943352, Vsync=757866609988, InputEventId=0, HandleInputStart=757882681239, AnimationStart=757882684884, PerformTraversalsStart=757883761306, DrawStart=757891283156, FrameDeadline=757133276684, FrameInterval=757882182116, FrameStartTime=16666666, SyncQueued=757893385202, SyncStart=757894204335, IssueDrawCommandsStart=757894287815, SwapBuffers=757935625144, FrameCompleted=758350913492, DequeueBufferDuration=4789, QueueBufferDuration=607949, GpuCompleted=758350857161, SwapBuffersCompleted=758350913492, DisplayPresentTime=319075656, 
D/ProfileInstaller: Installing profile for com.example.same312


```


after touching the button continues

```
W/native.stderr: s_glBindAttribLocation: bind attrib 0 name inPosition
W/native.stderr: s_glBindAttribLocation: bind attrib 1 name inColor
W/native.stderr: s_glBindAttribLocation: bind attrib 2 name inCircleEdge

```
