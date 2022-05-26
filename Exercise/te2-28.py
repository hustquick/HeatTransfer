import numpy as np
from functions import spherical_wall_R
from scipy.optimize import root

d = 1.22
delta = 0.45
lambda_ = 0.043
t_i = -62.2
t_o = 18
h_i = 1050
h_o = 21

#   做出以下假设：
#   1. 结冰的软木保温层由含水层和干软木保温层组成
#   2. 含水层的导热系数取冰的导热系数
#   3. 干软木保温层的导热系数取软木的导热系数
#   4. 含水（冰）软木保温层的厚度与之前相同


def expressions(p):
    delta_ice = p[0]
    r_1 = d / 2
    r_2 = d / 2 + delta_ice # delta_ice <= delta
    r_3 = d / 2 + delta

    area_i = 4 * np.pi * r_1**2
    area_o = 4 * np.pi * r_3**2

    R_i = 1 / (h_i * area_i)
    R_ice = spherical_wall_R(r_1, r_2, lambda_)
    R_wood = spherical_wall_R(r_2, r_3, lambda_)
    R_o = 1 / (h_o * area_o)

    R = R_i + R_ice + R_wood + R_o
    Phi = (t_o - t_i) / R
    t_2 = 0
    xpr = Phi - (t_o - t_2)/(R_wood + R_o)
    return xpr


guess_value = delta/2
delta_ice = root(expressions, guess_value).x[0]
print(f'结冰的冰软木保温层的厚度为：{delta_ice:.3f} m')
