# Matplotlib 中文绘图字体规范

项目中所有含中文的标题、坐标轴、图例或文字标注，均在创建图像前调用公共字体配置：

```python
import matplotlib.pyplot as plt
from Functions.Plotting import configure_chinese_font

configure_chinese_font()
fig, ax = plt.subplots()
ax.set_xlabel(r'传热系数($\mathrm{W/m^2 \cdot K}$)')
ax.set_ylabel(r'散热量($\mathrm{W}$)')
ax.set_title('散热量与传热系数的关系')
```

模块路径应沿用脚本现有的项目导入方式；从 `Problems` 或 `Examples` 目录运行时，需将项目根目录加入 `sys.path`。

## 统一配置

配置位于 `Functions/Plotting.py`，与原 `pr01-41.py` 设置一致：

```python
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = [
    'PingFang SC', 'Heiti SC', 'Microsoft YaHei', 'SimHei',
    'Noto Sans CJK SC', 'Arial Unicode MS', 'DejaVu Sans',
]
plt.rcParams['axes.unicode_minus'] = False
```

Matplotlib 按列表顺序查找可用字体。macOS 优先使用 PingFang SC（苹方）；Windows 可使用微软雅黑或 SimHei；Linux 可使用 Noto Sans CJK SC。最后的 DejaVu Sans 用于普通文字回退，并不保证支持中文。如果系统没有任何支持中文的候选字体，仍需安装中文字体。

`axes.unicode_minus=False` 使用普通减号显示负刻度，避免部分字体缺少 Unicode 负号。包含 LaTeX 反斜杠的标签使用原始字符串 `r'...'`。

## 后续编码要求

- 新增或修改含中文的图时，在创建图像前调用 `configure_chinese_font()`。
- 不在各题中重复维护字体列表，也不再单独指定 `SimHei`。
- 同一规则适用于 Python 脚本和 Jupyter 笔记本。
- 无须修改系统 `matplotlibrc`、向 Matplotlib 安装目录复制字体或删除整个缓存目录。
- 修改后实际绘制图像，检查标题、坐标轴、图例、标注以及缺字警告。
