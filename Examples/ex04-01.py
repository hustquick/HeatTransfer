import numpy as np

# 已知条件：教材 p.157，初值为零。
t = np.zeros(3)
eps = 5e-5

# 求解：高斯-赛德尔法，每求出一个温度就立即用于后面的方程。
print('迭代次数       t1          t2          t3')
print(f'{0:4d}', *[f'{v:11.5f}' for v in t])
for k in range(1, 101):
    t_old = t.copy()
    t[0] = (29 - 2*t[1] - t[2]) / 8
    t[1] = (32 - t[0] - 2*t[2]) / 5
    t[2] = (28 - 2*t[0] - t[1]) / 4
    print(f'{k:4d}', *[f'{v:11.5f}' for v in t])
    if np.max(np.abs(t - t_old)) < eps:
        break
else:
    raise RuntimeError('迭代未收敛')

# 输出：代回原方程检查残差。
A = np.array([[8, 2, 1], [1, 5, 2], [2, 1, 4]])
b = np.array([29, 32, 28])
print(f'最大方程残差 = {np.max(np.abs(A @ t - b)):.2e}')
