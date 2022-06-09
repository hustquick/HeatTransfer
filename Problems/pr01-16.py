import numpy as np
from scipy.optimize import fsolve

d = 25e-2
height = 175e-2
t = 30
h_1 = 15
t_a = 20
h_2 = 50

A = np.pi * d**2 / 4 + np.pi * d * height
Q_1 = h_1 * A * (t - t_a)
Q_2 = h_2 * A * (t - t_a)

guess_t_a2 = 25
t_a2 = fsolve(lambda t_a2: h_1 * (t - t_a2) - h_2 * (t - t_a), guess_t_a2)[0]
print(f'人体的散热量为：{Q_1:.2f} J')
print(f'有风的日子，人体的散热量为：{Q_2:.2f} J')
print(f'此时风冷温度为：{t_a2:.2f} C')
