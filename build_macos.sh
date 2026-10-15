#!/usr/bin/env bash
set -euo pipefail

# Run on an Intel Mac. PyInstaller cannot cross-compile from Linux or Windows.
if [[ "$(uname -s)" != "Darwin" || "$(uname -m)" != "x86_64" ]]; then
  echo "请在 Intel (x86_64) Mac 上执行此脚本。" >&2
  exit 1
fi

PYTHON_BIN="${PYTHON_BIN:-python3.11}"
"$PYTHON_BIN" -m venv .venv-macos
source .venv-macos/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt "pyinstaller>=6.10,<7"
python -m compileall -q run.py src

mkdir -p icon.iconset
for sz in 16 32 128 256 512; do
  sips -z "$sz" "$sz" assets/icon.png --out "icon.iconset/icon_${sz}x${sz}.png" >/dev/null
  dbl=$((sz * 2))
  sips -z "$dbl" "$dbl" assets/icon.png --out "icon.iconset/icon_${sz}x${sz}@2x.png" >/dev/null
done
iconutil -c icns icon.iconset -o assets/instaloader.icns

python -m PyInstaller --clean --noconfirm --windowed --onedir \
  --target-architecture x86_64 \
  --name "Instaloader GUI Wrapper" \
  --osx-bundle-identifier "io.github.rok1n.instaloaderguiwrapper" \
  --icon assets/instaloader.icns \
  --add-data "assets:assets" \
  --collect-all qdarktheme \
  --collect-submodules instaloader \
  run.py

APP="dist/Instaloader GUI Wrapper.app"
lipo -verify_arch x86_64 "$APP/Contents/MacOS/Instaloader GUI Wrapper"
codesign --force --deep --sign - "$APP"
codesign --verify --deep --strict "$APP"
mkdir -p dmg-root
rm -rf "dmg-root/Instaloader GUI Wrapper.app" dmg-root/Applications
ditto "$APP" "dmg-root/Instaloader GUI Wrapper.app"
ln -s /Applications dmg-root/Applications
hdiutil create -volname "Instaloader GUI Wrapper" -srcfolder dmg-root \
  -ov -format UDZO "Instaloader-GUI-Wrapper-macOS-Intel-x86_64-zh-CN.dmg"
shasum -a 256 "Instaloader-GUI-Wrapper-macOS-Intel-x86_64-zh-CN.dmg" \
  > "Instaloader-GUI-Wrapper-macOS-Intel-x86_64-zh-CN.dmg.sha256"
echo "构建完成：Instaloader-GUI-Wrapper-macOS-Intel-x86_64-zh-CN.dmg"
