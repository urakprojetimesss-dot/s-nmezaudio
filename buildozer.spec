[app]
title = Sonmez Audio
package.name = sonmezaudio
package.domain = org.sonmez

source.dir = .
source.include_exts = py,png,jpg,kv,atlas
source.exclude_exts = spec
source.exclude_dirs = tests, bin, venv

version = 0.1
requirements = python3==3.10.11,kivy==2.2.1

orientation = portrait
fullscreen = 0

android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
