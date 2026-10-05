import numpy as np

# 已知条件：教材 p.158，节点按图示为上排 1、2，下排 3、4。
t_top = 500
t_left = t_right = t_bottom = 100
t = np.array([300., 300., 200., 200.])
eps = 2e-4

# 求解：等步长、无内热源，各内节点温度等于四邻点温度平均值。
print('迭代次数      t1          t2          t3          t4 / °C')
print(f'{0:4d}', *[f'{v:11.5f}' for v in t])
for k in range(1, 101):
    t_old = t.copy()
    t[0] = (t_top + t_left + t[1] + t[2]) / 4
    t[1] = (t_top + t_right + t[0] + t[3]) / 4
    t[2] = (t_bottom + t_left + t[0] + t[3]) / 4
    t[3] = (t_bottom + t_right + t[1] + t[2]) / 4
    print(f'{k:4d}', *[f'{v:11.5f}' for v in t])
    if np.max(np.abs((t - t_old) / t)) < eps:
        break
else:
    raise RuntimeError('迭代未收敛')

# 输出
print('稳态极限：t1 = t2 = 250 °C，t3 = t4 = 150 °C')
