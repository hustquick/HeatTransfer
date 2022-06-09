import numpy as np

A = 12
t_eva = 0
t_i = 9.7
t_o = 5
Q = 6900

delta_T = np.average([t_i, t_o]) - t_eva
h = Q / (A * delta_T)
print(f'总传热系数为：{h:.2f} W/m^2-K')
