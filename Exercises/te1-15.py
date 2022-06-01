import numpy as np

q = 3500
t_a = 45
t_w = 80
d_o = 36e-3
delta = 2e-3

d_i = d_o - 2*delta
A_o = np.pi * d_o
A_i = np.pi * d_i
h = q * A_o / (A_i * (t_w - t_a))
print(f'截面上的局部表面传热系数为：{h:.2f} W/m2-K')
