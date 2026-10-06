import numpy as np

d = 25e-2
height = 175e-2
t = 30
h_1 = 15
t_a = 20
h_2 = 50

A = np.pi * d**2 / 4 + np.pi * d * height
Q_1 = h_1 * A * (t - t_a)
Q_2 = h_2 * A * (t - t_a)

# 相同散热功率：h_1*(t - t_a2) = h_2*(t - t_a)，直接解线性方程。
t_a2 = t - h_2 / h_1 * (t - t_a)
print(f'人体的散热功率为：{Q_1:.2f} W')
print(f'有风的日子，人体的散热功率为：{Q_2:.2f} W')
print(f'此时风冷温度为：{t_a2:.2f}degC')
