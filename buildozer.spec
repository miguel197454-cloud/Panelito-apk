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
android.api = 33
android.minapi = 21
android.build_tools = 34.0.0

android.archs = arm64-v8a, armeabi-v7a

android.permissions = INTERNET

# =========================
# OPTIONAL (keep simple for now)
# =========================
# android.enable_androidx = True
# android.wakelock = False

# =========================
# PYTHON FOR ANDROID
# =========================
# (leave defaults)
