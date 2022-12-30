import numpy as np
import sys
sys.path.append("..")
from Functions.SteadyStateConduction import spherical_wall_R
from scipy.optimize import root

r = 1.8
delta = 0.5
lambda_ = 0.15
t_oo = -40
h_o = 15
h_i = 6
t_ground = -20
Phi = 960


def expressions(p):
    t = p[0]
    area_ground = np.pi * (r**2)
    Phi_ground = h_i * area_ground * (t - t_ground)

    r_m = r + delta / 2

    R_2 = spherical_wall_R(r, r+delta, lambda_)
    R_1 = 1 / (h_i * (2 * np.pi * r**2))
    R_3 = 1 / (h_o * (2 * np.pi * (r+delta)**2))

    R_roof = R_1 + R_2 + R_3
    Phi_roof = (t - t_oo) / R_roof
    xpr = Phi_ground + Phi_roof - Phi
    return xpr


guess_value = [t_ground+1]
t = root(expressions, guess_value).x[0]
print(f'小屋内的空气平均温度为：{t:.2f}degC')
