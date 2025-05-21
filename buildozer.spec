[app]

# (str) Title of your application
title = MyApp

# (str) Package name
package.name = myapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (str) Main .py file
source.main = main.py

# (list) List of inclusions using pattern matching
source.include_exts = py,png,jpg,kv,atlas,html,js,css

# (str) Application versioning
version = 0.1

# (str) Application requirements
requirements = python3,kivy

# (str) Supported orientation (one of: landscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (str) Presplash of the application
presplash.filename = %(source.dir)s/data/presplash.png

# (list) Permissions
android.permissions = INTERNET

# (int) Target API (minimum 21 for modern Android)
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (int) Android NDK version to use
android.ndk = 25b

# (bool) Enable AndroidX support
android.enable_androidx = True

# (str) Bootstrap to use
p4a.bootstrap = sdl2

# (str) Entry point for the app
android.entrypoint = org.kivy.android.PythonActivity

# (str) Icon of the application
icon.filename = %(source.dir)s/data/icon.png

# (str) Supported architectures
android.archs = armeabi-v7a, arm64-v8a

# (bool) Copy library instead of compiling (for testing only)
# android.copy_libs = 1

# (str) Path to build artifacts (build folder)
# build.dir = ./build

# (str) Path to the dist folder
# dist.dir = ./dist

# (bool) Use gradle instead of ant
android.use_gradle = True

# (list) Command line options to pass to gradle
# android.gradle_dependencies = com.google.android.material:material:1.4.0

# (str) Custom java package for android
# android.package = org.myapp

# (str) Custom application class for android
# android.application_class = org.kivy.android.PythonApplication

# (bool) Hide loading screen
android.hide_loading_screen = False

# (str) Path to custom Java .java source files (if any)
# android.add_src = src

# (list) Put these files or folders in the .apk
# android.add_assets = assets

# (list) Gradle dependencies to add
# android.gradle_dependencies = 

# (list) Add jars to build classpath
# android.add_jars = libs/*.jar

# (list) Add Java modules to source
# android.add_java_modules =

# (str) Path to Java classes to include in .apk
# android.add_classes =

# (list) Gradle properties to set
# android.gradle_properties =

# (str) Keystore file to sign app
# android.keystore = my.keystore

# (str) Key alias
# android.keyalias = mykeyalias

# (str) Key password
# android.keypassword = mykeypassword

# (str) Keystore password
# android.keystore_password = mykeystorepassword

# (bool) Create a big .apk with all architecture
android.multiarch = 1

# (str) Path to local.properties
# android.local_properties = local.properties

# (str) Directory where .java/.kt source files will be copied before compiling
# android.java_src_dir = 

# (str) Custom environment variables for p4a
# p4a.custom_env = 

# (list) Whitelist of files to include (glob patterns)
# source.include_patterns = assets/*,images/*.png

# (list) Blacklist of files to exclude (glob patterns)
# source.exclude_patterns = license,images/*/*.jpg

# (bool) Use --private data storage (do not use unless necessary)
# android.private_storage = False

# (str) Custom Java class for main activity
# android.activity_class_name =

# (str) Use this Java class as the app entry point
# android.entrypoint_class_name =

# (str) Custom package to override the default one
# android.custom_package = 

[buildozer]

# (str) Log level (1 = error, 2 = warn, 3 = info, 4 = debug (default), 5 = trace)
log_level = 2

# (int) Number of concurrent jobs
num_workers = 2

# (str) Directory to store the build
build_dir = ./.buildozer

# (str) Python interpreter to use
python = python3

# (bool) Automatically accept sdk licenses
accept_sdk_license = True

extra_env = CFLAGS=-I/data/data/com.termux/files/usr/include LDFLAGS=-L/data/data/com.termux/files/usr/lib
