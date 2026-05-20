[app]

title = Sanzo Quiz
package.name = sanzoquiz
package.domain = org.lwcode

source.dir = .
source.include_exts = py,png,jpg,kv,wav

version = 1.0

requirements = python3,kivy,kivymd,pillow

orientation = portrait

fullscreen = 1


android.api = 33
android.minapi = 24
android.sdk = 33
android.ndk = 25b

android.permissions = INTERNET,VIBRATE

android.accept_sdk_license = True

[buildozer]

log_level = 2
warn_on_root = 1