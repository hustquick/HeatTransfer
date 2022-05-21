import numpy as np

d = 50e-3
l = 300e-3
lambda_ = 50
t_1 = 60
t_2 = 20

A = np.pi * d**2 / 4
Phi = lambda_ * A * (t_1 - t_2) / l
print(f'Phi = {Phi:.2f} W') # 课本结果有误