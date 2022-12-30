# 可看做两个断面绝热的等截面弯肋的叠加
import numpy as np
import sys
sys.path.append("..")
from Functions.SteadyStateConduction import fin_tip_R, fin_tip_Delta_T_ratio, fin_tip_efficiency

d = 25e-3
theta = np.pi
R = 75e-3
t_w = 80
t_f = 20
h = 10
lambda_ = 1.5

R_p = R - d/2
H = theta * R_p / 2
r = d/2
A_c = np.pi * r**2
perimeter = np.pi * d

R = fin_tip_R(H, perimeter, A_c, lambda_, h)
Phi = 2 * (t_w - t_f) / R
print(f'手柄的散热量为{Phi:.2f} W')

eta = fin_tip_efficiency(H, perimeter, A_c, lambda_, h)
Delta_T_ratio = fin_tip_Delta_T_ratio(H, perimeter, A_c, lambda_, h)
t_min = t_f + Delta_T_ratio * (t_w - t_f)
print(f'手柄的最低温度为{t_min:.2f}degC')
print(f'手柄的导热系数越大，散热量越大，手柄每一截面处的温度也越均匀。')
