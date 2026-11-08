"""从 Google Noto CJK 官方仓库下载可再分发的简体中文字体。"""
from pathlib import Path
from urllib.request import urlopen

URL = (
    "https://raw.githubusercontent.com/notofonts/noto-cjk/main/"
    "Sans/OTF/SimplifiedChinese/NotoSansCJKsc-Regular.otf"
)
TARGET = Path(__file__).resolve().parents[1] / "Functions" / "fonts" / "NotoSansCJKsc-Regular.otf"


def main():
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    print(f"Downloading Noto Sans CJK SC from {URL}")
    with urlopen(URL, timeout=90) as response:
        data = response.read()
    if len(data) < 100_000 or data[:4] not in (b"OTTO", b"\x00\x01\x00\x00"):
        raise RuntimeError("下载内容不是有效的 OpenType/TrueType 字体，未覆盖现有文件。")
    temp = TARGET.with_suffix(".tmp")
    temp.write_bytes(data)
    temp.replace(TARGET)
    print(f"Font installed: {TARGET} ({len(data)} bytes)")
    print("License: SIL OFL 1.1 — https://openfontlicense.org/")


if __name__ == "__main__":
    main()
