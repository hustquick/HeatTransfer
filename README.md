# HeatTransfer

《传热学（第五版）》（陶文铨）部分例题及课后习题的 Python 解法。项目用于学习传热学、核对计算过程，以及继续完善数值计算和绘图代码，并非教材全部题目的完整答案。

计算方法包括方程求解、物性查询、查表与插值、积分、常微分方程、符号计算、有限差分和结果绘图。

## 项目结构

| 目录或文件 | 内容 |
| --- | --- |
| `Examples/` | 教材例题，例如 `ex03-12.py` |
| `Problems/` | 课后习题，例如 `pr01-41.py` |
| `Functions/` | 导热计算、辅助函数和公共绘图配置 |
| `Appendix/` | 物性数据和查表函数 |
| `Batch_test/test_examples.py` | 批量运行现有例题 |
| `Batch_test/test_problems.py` | 批量运行现有习题 |
| `jupyter/` | 按章节整理的 Jupyter 笔记本 |
| `requirements.txt` | Python 依赖列表 |
| `AGENTS.md` | 后续代码修改约定 |

## 安装与环境

需要 Python 3，以及 NumPy、SciPy、CoolProp、SymPy 和 Matplotlib。目前本地已使用 Python 3.14.8 验证两个批量脚本，依赖版本未锁定。

下载项目并进入项目根目录：

```sh
git clone https://github.com/hustquick/HeatTransfer.git
cd HeatTransfer
```

推荐使用虚拟环境。macOS / Linux：

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Windows PowerShell：

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

下面的命令均使用已激活环境中的 `python`。如果没有激活环境，也可以使用虚拟环境 Python 的完整路径运行。

## 运行单道题

题目根据脚本位置定位项目根目录，可从不同工作目录启动。下面进入题目目录运行，使 PDF 输出也保存在题目目录。

运行一道例题：

```sh
cd Examples
python ex03-12.py
```

运行一道习题（从项目根目录开始）：

```sh
cd Problems
python pr01-41.py
```

有绘图的题目会显示图窗；单题运行时，关闭图窗后程序结束。调用 `Functions.Plotting.save_pdf(name, fig)` 的题目还会将同名 PDF 保存到当前工作目录，例如 `Problems/pr01-41.pdf`。PDF 和 Python 缓存已由 `.gitignore` 排除。

## 批量计算与绘图

从项目根目录运行：

```sh
python Batch_test/test_examples.py
python Batch_test/test_problems.py
```

两个批量脚本会根据自身位置找到题目目录，不依赖启动时的工作目录。运行行为如下：

1. 按文件名排序，依次运行相应目录中的全部 `.py` 文件。
2. 在当前 Python 进程中执行各题，沿用启动脚本的 Python 环境。
3. 计算过程中保留生成的图，暂时跳过各题的 `plt.show()` 等待。
4. 全部题目处理完成后，打印“运行完毕”，统一显示所有仍然存在的图窗。
5. 某题发生普通运行异常时，打印错误并继续后续题目；最后列出失败题目。

因此，无须逐题关闭图窗才能继续计算。最后显示图窗时，程序仍会等待窗口关闭。“运行完毕”表示批量处理已结束，是否有失败题目应同时查看失败列表。题目输出中的适用条件提醒仍需按物理意义判断。

## VS Code 使用

用 VS Code 打开整个 `HeatTransfer` 文件夹，然后执行 **Python: Select Interpreter**，选择已安装项目依赖的虚拟环境。

单题运行时，注意终端工作目录应为 `Examples` 或 `Problems`。也可在本机工作区设置中使用：

```json
{
  "python.terminal.executeInFileDir": true,
  "code-runner.fileDirectoryAsCwd": true
}
```

如果使用 Code Runner，其 Python 执行器需单独指定为所选环境的 Python 路径；仅选择 Python 扩展的解释器，不一定会更新 Code Runner。遇到 `python: command not found`，请检查终端是否激活环境，以及 Code Runner 的 `code-runner.executorMap` 设置。

本机解释器绝对路径应保留在个人设置中，不应作为项目通用配置提交。

## 中文绘图

中文字体统一由 [Functions/Plotting.py](Functions/Plotting.py) 配置。在项目模块可正常导入的前提下，创建含中文的图之前调用：

```python
import matplotlib.pyplot as plt
from Functions.Plotting import configure_chinese_font

configure_chinese_font()
fig, ax = plt.subplots()
ax.set_xlabel(r'传热系数($\mathrm{W/m^2 \cdot K}$)')
ax.set_ylabel(r'散热量($\mathrm{W}$)')
ax.set_title('散热量与传热系数的关系')
```

字体候选顺序为 `PingFang SC`、`Heiti SC`、`Microsoft YaHei`、`SimHei`、`Noto Sans CJK SC`、`Arial Unicode MS`、`DejaVu Sans`。Matplotlib 会按顺序使用可用字体；系统仍需至少安装一种支持中文的候选字体，最后的 DejaVu Sans 不保证覆盖中文。

这套配置适用于 macOS、Windows 和 Linux，无须修改系统 `matplotlibrc`。新增中文图时复用公共函数，不在各题中重复维护字体列表。详细说明见 [解决matplotlib中文乱码问题.md](解决matplotlib中文乱码问题.md)。

## Jupyter 笔记本

笔记本位于 `jupyter/`。若环境尚未安装 Jupyter，可在同一虚拟环境中运行：

```sh
python -m pip install jupyterlab
python -m jupyter lab
```

建议从项目根目录启动，并选择安装了项目依赖的内核，按单元格顺序运行。批量脚本只运行 Python 题目文件，不执行笔记本；笔记本中已有输出不会随着脚本修改自动更新，需要重新执行相应单元格。

## 继续完善项目

- 新增题目沿用 `ex章节-题号.py` 或 `pr章节-题号.py` 的命名方式。
- 标明已知条件、单位、公式及适用范围；条件缺失或自行假设时写明依据。
- SciPy 求解器可能向回调传入 NumPy 数组，涉及误差函数时使用 `scipy.special.erf` / `erfc`。
- 修改题目后运行该题；修改公共计算函数或批量脚本后，运行受影响的批量检查。
- 遵循 [AGENTS.md](AGENTS.md) 中的中文绘图约定。
- 核对教材时，以题设、公式和实际计算为依据；批量运行无异常并不等于计算结果已经全部经过教材校验。

项目许可证见 [LICENSE](LICENSE)。
