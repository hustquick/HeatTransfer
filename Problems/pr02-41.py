import numpy as np
from scipy.optimize import root

import sys
sys.path.append("..")
from Functions.SteadyStateConduction import cylinder_Delta_T_with_heat_source, cylindrical_wall_R


t_max = 1600
t_water = 110
h = 12000
R_c = 2.2e-4    # m^2-K/W
r_1 = 6.1e-3
r_2 = 6.5e-3
lambda_ = 7.9
lambda_alloy = 14.2


def expressions(p):
    phi = p
    q_dot = phi / (np.pi * r_1**2)
    t_w = t_max - cylinder_Delta_T_with_heat_source(r_1, lambda_, q_dot)
    R_w = cylindrical_wall_R(r_1, r_2, lambda_, 1)
    R_conv = 1 / (h * 2*np.pi*r_2)
    R = R_c / (2*np.pi*r_1) + R_w + R_conv  # R_c的单位表明其需要除以接触面积
    xpr = phi - (t_w - t_water) / R
    return xpr


guess_values = 1e6
phi = root(expressions, guess_values).x[0]
print(f'最大热功率为：{phi:.2f} W')
