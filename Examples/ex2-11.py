import numpy as np

d = 250e-3
a, b = 500e-3, 500e-3
t_s = 200
t_insu = 60
lambda_ = 0.08
length = 2

# 形状因子
S = 2 * np.pi * length / (np.log(1.08*b/d))
Phi = S * lambda_ * (t_s - t_insu)
print(f'Phi = {Phi:.2f} W')
