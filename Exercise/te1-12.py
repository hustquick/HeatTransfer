import numpy as np

t_w = 69
t_f = 20
d = 14e-3
l = 80e-3
P = 8.5

A = np.pi * d * l
h = P / (A * (t_w - t_f))
print(f'对流传热表面传热系数为：{h:.2f} W/(m^2-K)')
