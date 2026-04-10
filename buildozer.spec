[app]

title = My Application
package.name = myapp
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

requirements = python3,kivy

orientation = portrait
fullscreen = 0

# =========================
# ANDROID CONFIG (FIXED)
# =========================
android.api = 34
android.minapi = 21
android.build_tools_version = 34.0.0

android.archs = arm64-v8a, armeabi-v7a

android.permissions = INTERNET

# =========================
# OPTIONAL (SAFE DEFAULTS)
# =========================
# android.enable_androidx = True
# android.wakelock = False
# android.private_storage = True
