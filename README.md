# HeatTransfer

#### 介绍
传热学第六版例题及课后计算题的Python解法。

#### 数据处理过程
1. 自定义函数
2. 使用物理常量
3. 解方程（组）
4. 利用表格查值
5. 利用表格插值
6. 微积分
7. 求解给定初始条件和边界条件的常微分方程
8. 符号运算
9. 物性参数查询
10. 绘图


#### 使用教程

1. 在[Python官网](https://www.python.org)下载3.8以下的Python 3版本（本项目所有计算均在Python 3.6的环境下编译完成。由于**CoolProp库仅支持3.8以下Python 3的版本**，以上解题过程可能在更高版本的python中无法正常运行。），并安装。
2. 推荐使用[PyCharm](https://www.jetbrains.com/pycharm/)运行本项目中的代码。
3. 安装的第三方库包括：numpy, scipy, matplotlib, sympy, coolprop。第三方库的安装方法，可以利用pip或者conda等工具进行安装（在命令行工具中输入`pip install numpy sicpy matplotlib sympy coolprop`或`pip install numpy sicpy matplotlib sympy coolprop`），也可以利用PyCharm的Python Packages包管理器安装这些第三方包。
4. 下载本项目的所有文件到本地计算机。想要查看特定题目的结果，可以直接运行该题目的py文件。
5. 也可以运行test文件夹下的[test_examples.py](https://gitee.com/hustquick/heat-transfer/blob/master/test/test_examples.py)文件来求解所有例题，运行test文件夹下的[test_problems.py](https://gitee.com/hustquick/heat-transfer/blob/master/test/test_problems.py)文件来求解所有习题。
6. 对于Windows系统，如果下载的文件无法正常运行，则需要将下载下来的HeatTransfer文件夹路径添加至**系统路径**(**path**)。
