# 解决macOS 和 Linux系统中matplotlib 中文乱码问题

## 1. 先修改 matplotlibrc 文件

运行以下代码，进入vim   
```python
import os
import matplotlib
st = 'vim ' + matplotlib.matplotlib_fname()
os.system(st)
```
   
在 vim 中使用`/font.family`命令找到#font.family所在行，将`#font.family`前的`#`去掉；

使用`/font.sans-serif`命令找到#font.sans-serif所在行，[将`#font.sans-serif`前的`#`去掉，并加上`SimHei`字体](https://cdn.jsdelivr.net/gh/hustquick/figures@master/uPic/R8dkS7.png)；

使用`/axes.unicode_minus`命令找到[#axes.unicode_minus](https://cdn.jsdelivr.net/gh/hustquick/figures@master/uPic/4wvvQf.png)所在行，[将`#axes.unicode_minus`前的`#`去掉，并把`True`改为`False`](https://cdn.jsdelivr.net/gh/hustquick/figures@master/uPic/ndCghW.png)。

输入`:x`命令，保存并退出。

## 2. 将 SimHei.ttf 文件复制到 matplotlib 的字体文件夹

a. 将以下代码保存为copy_SimHei.py文件
   
```python
import os
import matplotlib
path = matplotlib.get_data_path() + '/fonts/ttf/SimHei.ttf'
st = 'cp SimHei.ttf ' + path
os.system(st)
```
 
b. 在网站[xiazaiziti](http://www.xiazaiziti.com/210356.html)上下载 SimHei.ttf 文件，并将其移动到 copy_SimHei.py 所在文件夹；
      
c. 运行 copy_SimHei.py 文件。
   
## 3. 重新加载字体

运行以下代码
   
```python
import shutil
import matplotlib
shutil.rmtree(matplotlib.get_cachedir())  
```
安装了字体后，在 matplotlib 里使用的中文字符串，前面不需要再加 u ，也不需要再在代码里定义字体。​   

## 4. 测试

运行以下测试代码

```python
# 随便绘制一个饼图
import matplotlib.pyplot as plt
 
fig1 = plt.figure()  # 先创建一个图像对象
plt.pie([0.5, 0.3, 0.2],  # 值
        labels=['我', '你', '它'],  # 标签
        explode=(0, 0.2, 0),  # （爆裂）距离
        autopct='%1.1f%%',   # 显示百分数格式
        shadow=True)  # 是否显示阴影
plt.show()
```

观察中文字符是否不再是乱码。

# 解决 Windows 中的 matplotlib 中文乱码问题

## 1. 先修改 matplotlibrc 文件

运行以下代码，进入vim   
```python
import os
import matplotlib
st = 'vim ' + matplotlib.matplotlib_fname()
os.system(st)
```
   
在 vim 中使用`/font.family`命令找到#font.family所在行，将`#font.family`前的`#`去掉；

使用`/font.sans-serif`命令找到#font.sans-serif所在行，[将`#font.sans-serif`前的`#`去掉，并加上`SimHei`字体](https://cdn.jsdelivr.net/gh/hustquick/figures@master/uPic/R8dkS7.png)；

使用`/axes.unicode_minus`命令找到[#axes.unicode_minus](https://cdn.jsdelivr.net/gh/hustquick/figures@master/uPic/4wvvQf.png)所在行，[将`#axes.unicode_minus`前的`#`去掉，并把`True`改为`False`](https://cdn.jsdelivr.net/gh/hustquick/figures@master/uPic/ndCghW.png)。

输入`:x`命令，保存并退出。

## 2. 将 SimHei.ttf 文件复制到 matplotlib 的字体文件夹

a. 将以下代码保存为copy_SimHei.py文件
   
```python
import os
import matplotlib
path = matplotlib.get_data_path() + '\\fonts\\ttf\\SimHei.ttf'
st = 'copy SimHei.ttf ' + path
os.system(st)
```
b. 在网站[xiazaiziti](http://www.xiazaiziti.com/210356.html)上下载 SimHei.ttf 文件，并将其移动到 copy_SimHei.py 所在文件夹；
    
c. 运行 copy_SimHei.py 文件。

## 3. 测试

运行以下测试代码

```python
# 随便绘制一个饼图
import matplotlib.pyplot as plt
 
fig1 = plt.figure()  # 先创建一个图像对象
plt.pie([0.5, 0.3, 0.2],  # 值
        labels=['我', '你', '它'],  # 标签
        explode=(0, 0.2, 0),  # （爆裂）距离
        autopct='%1.1f%%',   # 显示百分数格式
        shadow=True)  # 是否显示阴影
plt.show()
```

观察中文字符是否不再是乱码。
