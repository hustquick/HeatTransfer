"""项目统一的 Matplotlib 中文字体配置。"""
from pathlib import Path
import warnings

import matplotlib.pyplot as plt
from matplotlib import font_manager

_FONT_CANDIDATES = (
    "PingFang SC", "Heiti SC", "Microsoft YaHei", "SimHei",
    "Noto Sans CJK SC", "Source Han Sans SC", "WenQuanYi Micro Hei",
    "Arial Unicode MS",
)
# 这些字形用于检查字体确实覆盖常见简体中文，而不只是名称匹配。
_SAMPLE_TEXT = "中文传热温度效率"
_BUNDLED_FONT = Path(__file__).resolve().parent / "fonts" / "NotoSansCJKsc-Regular.otf"


def _supports_chinese(font_path):
    """使用 Matplotlib 自带的 FreeType 接口检查实际字形覆盖。"""
    try:
        from matplotlib.ft2font import FT2Font
        font = FT2Font(str(font_path))
        return all(font.get_char_index(ord(char)) != 0 for char in _SAMPLE_TEXT)
    except (OSError, RuntimeError, ValueError):
        return False


def configure_chinese_font():
    """选择可用中文字体；系统缺失时使用项目自带的 Noto Sans CJK SC。

    返回实际选择的字体名称。缺少中文字体时抛出明确异常，
    避免静默生成方框。应在创建图像前调用。
    """
    available = {}
    for entry in font_manager.fontManager.ttflist:
        available.setdefault(entry.name, []).append(entry.fname)

    selected = None
    for name in _FONT_CANDIDATES:
        if any(_supports_chinese(path) for path in available.get(name, ())):
            selected = name
            break

    if selected is None and _BUNDLED_FONT.is_file():
        if _supports_chinese(_BUNDLED_FONT):
            font_manager.fontManager.addfont(str(_BUNDLED_FONT))
            selected = font_manager.FontProperties(fname=str(_BUNDLED_FONT)).get_name()
        else:
            warnings.warn(f"内置字体无法加载或缺少中文字形：{_BUNDLED_FONT}", RuntimeWarning)

    if selected is None:
        raise RuntimeError(
            "未找到可用的中文字体。请运行 "
            "'python scripts/install_chinese_font.py' 安装项目字体，"
            "或安装 Noto Sans CJK SC / 思源黑体后重新运行。"
        )

    plt.rcParams["font.family"] = "sans-serif"
    plt.rcParams["font.sans-serif"] = [selected, "DejaVu Sans"]
    plt.rcParams["axes.unicode_minus"] = False
    return selected


def save_pdf(name, fig):
    """保存指定图像为 PDF；显示图窗由调用方负责。"""
    fig.savefig(f"{name}.pdf")
