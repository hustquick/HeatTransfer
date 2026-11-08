# 中文字体资源

本目录用于存放 `NotoSansCJKsc-Regular.otf`，作为系统缺少中文字体时的回退资源。

运行 `python scripts/install_chinese_font.py` 可从 Google Noto CJK 官方仓库下载该字体。下载后可将字体文件加入项目发行包，供离线用户使用。**本次提交不包含字体二进制文件**，因此全新克隆的项目在无中文系统字体、且无法联网下载时仍会给出明确错误。

字体版权归原权利人所有，采用 SIL Open Font License 1.1。再分发时应随字体保留原始版权与许可证文本；详见 https://github.com/notofonts/noto-cjk 。
