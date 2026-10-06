"""项目统一的 Matplotlib 中文字体配置。"""
import matplotlib.pyplot as plt


def configure_chinese_font():
    """绘图前调用，按顺序使用系统中可用的字体。"""
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = [
        'Heiti SC', 'PingFang SC', 'Microsoft YaHei', 'SimHei',
        'Noto Sans CJK SC', 'Arial Unicode MS', 'DejaVu Sans',
    ]
    plt.rcParams['axes.unicode_minus'] = False
