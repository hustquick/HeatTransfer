# 项目代码约定

## 中文绘图

新增或修改包含中文标题、坐标轴、图例或文字标注的 Matplotlib 图时，在创建图像前导入并调用 `Functions.Plotting.configure_chinese_font()`。Python 脚本和 Jupyter 笔记本均遵循此规则。

字体列表统一维护在 `Functions/Plotting.py`，不要在各题中复制配置或单独指定 SimHei。包含 LaTeX 反斜杠的标签使用原始字符串。修改后实际绘图检查中文显示及缺字警告。

详细配置与使用示例见 [解决matplotlib中文乱码问题.md](解决matplotlib中文乱码问题.md)。
