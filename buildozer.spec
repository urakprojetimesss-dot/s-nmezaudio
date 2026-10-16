[app]
title = Sonmez Audio
package.name = sonmezaudio
package.domain = org.sonmez
source.include_exts = py,png,jpg,kv,atlas
source.dir = .
version = 0.1
requirements = python3,kivy,sounddevice,numpy
orientation = portrait
osx.python_version = 3
fullscreen = 0
android.permissions = RECORD_AUDIO,MODIFY_AUDIO_SETTINGS,INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
