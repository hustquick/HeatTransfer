from Functions.SteadyStateConduction import fin_tip_R
import numpy as np

material = 'Al'
t_w = 260
d = 25e-3
H = 150e-3
t_1 = 16
h = 15

perimeter = np.pi * d
A_c = np.pi * d**2 / 4
lambda_ = 208   # 采用上一题给出Al的导热系数

R = fin_tip_R(H, perimeter, A_c, lambda_, h)
Phi = (t_w - t_1) / R
print(f'Phi2 = {Phi:.2f} W')

H_2 = 2*H
R_2 = fin_tip_R(H_2, perimeter, A_c, lambda_, h)
Phi_2 = (t_w - t_1) / R_2
print(f'Phi2 = {Phi_2:.2f} W')
