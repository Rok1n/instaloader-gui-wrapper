# Instaloader GUI Wrapper（简体中文 / Intel macOS）

这是 [marhensa/instaloader-gui-wrapper](https://github.com/marhensa/instaloader-gui-wrapper) 的中文与 macOS Intel 适配版本，基于 PyQt6 和 Instaloader，保留原项目的 Instagram 下载功能。

## 主要功能

- 目标账号下载：帖子、快拍、精选动态和头像
- 下载自己收藏的帖子，以及单个帖子 / Reels / 快拍链接
- 用户名密码登录、已有会话文件登录、双重验证（2FA）
- 日期范围、数量限制、跳过重复、文件夹分类
- 下载进度、图像预览、请求间隔与限速保护
- 简体中文界面、状态消息和安装说明

## 安装 Intel Mac 版

从本仓库的 [Releases](https://github.com/Rok1n/instaloader-gui-wrapper/releases) 下载名称中含 `macOS-Intel-x86_64-zh-CN.dmg` 的文件。

1. 双击 DMG，将 `Instaloader GUI Wrapper.app` 拖入 `Applications`（应用程序）文件夹。
2. 从应用程序中打开。首次运行如遇“无法验证开发者”提示，打开「系统设置 → 隐私与安全性」，在确认来源可信后允许打开。
3. 此分发包目前使用临时（ad-hoc）签名，**尚无 Apple Developer ID 签名与 Apple 公证**。不应宣称是经过 Apple 公证的版本。

Intel Mac 架构：`x86_64`，无需 Rosetta 2。此 DMG **不是** Apple Silicon (M1/M2/M3/M4) 原生包。CI 使用 GitHub 的 `macos-15-intel` 执行器，因此早于 macOS 15 的系统兼容性需在真实设备上另行验证。

**数据路径（macOS）：**
- 默认下载目录：`~/Downloads`（可在界面中自定义）
- 配置文件：`~/Library/Application Support/Instaloader-GUI-Wrapper/settings.json`
- 日志：`~/Library/Application Support/Instaloader-GUI-Wrapper/instagram_downloader.log`
- 会话文件：`~/.config/instaloader/session-用户名`，或选择现有会话文件。

## 在 Intel Mac 上自行构建

需要 macOS、Intel CPU、Python 3.11，以及 Xcode Command Line Tools（提供 `sips`、`iconutil`、`hdiutil`）。

```bash
git clone https://github.com/Rok1n/instaloader-gui-wrapper.git
cd instaloader-gui-wrapper
chmod +x build_macos.sh
./build_macos.sh
```

构建完成后，DMG 位于项目根目录。

## 自动构建 / 发布

代码提交到 `main` 或构建分支会触发 [Actions](https://github.com/Rok1n/instaloader-gui-wrapper/actions) 中的 **Build Intel macOS DMG**。构建成功的 DMG 会作为 Actions Artifact 上传，可下载测试。推送 `v*` 标签或成功构建 `main` 后，会自动生成 GitHub 预发布版（Prerelease）。

请注意：CI 成功仅代表依赖安装、语法检查、二进制架构校验、应用打包及 DMG 生成成功；Instagram 登录及下载功能仍应在真实 Intel Mac 上测试。

## 源码运行

本项目依赖的 `pyqtdarktheme` 目前不能安装在 Python 3.12，推荐 Python 3.11：

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python run.py
```

## 安全与版权

请遵守 Instagram 的服务条款及内容版权要求。请勿分享 Instagram 会话文件。批量下载可能触发平台的访问限制。原项目许可与作者归属信息保留；如原仓库没有单独的 LICENSE 文件，原始版权和许可声明可见 README 与源码文件头。
