import numpy as np

import sys
sys.path.append("..")
from Functions.SteadyStateConduction import fin_tip_efficiency2


material = 'Al'
d = 25e-3
s = 9.5e-3
H = 12.5e-3
delta = 0.8e-3
t_w = 200
t_f = 90
h = 110
lambda_ = 208   # 参考题2-50取值
length = 1

H_p = H + delta/2
A_L = H_p * delta
fin_efficiency = fin_tip_efficiency2(H, A_L, lambda_, h)
fin_area = 2 * np.pi * ((d/2+H_p)**2 - (d/2)**2)
Phi_fin = fin_efficiency * h * fin_area * (t_w - t_f)
base_area = np.pi * d * (s - delta)
Phi_base = h * base_area * (t_w - t_f)
number = length / s
Phi = number * (Phi_fin + Phi_base)

print(f'总散热量为：{Phi:.2f} W')

# 也可以采用overall_fin_surface_efficiency函数求解
# eta = overall_fin_surface_efficiency(fin_area, base_area, fin_efficiency)
# Phi = eta * h * (fin_area + base_area) * (t_w - t_f) * number
# print(f'总散热量为：{Phi:.2f} W')

