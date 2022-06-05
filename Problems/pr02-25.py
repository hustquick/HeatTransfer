import numpy as np
from Functions.SteadyStateConduction import spherical_wall_R
from scipy.optimize import root

d_i = 0.5
d_o = 0.6
Phi_dot = 1e5   # W/m^3
h = 1000        # W/m^2-K
t_f = 25
material = '铬镍钢'

temperature_list = [-100, 0, 100, 200, 300, 400, 600, 800]
lambda_list = [12.2, 14.7, 16.6, 18.0, 19.4, 20.8, 23.5, 26.3]


def lambda_(t):
    return np.interp(t, temperature_list, lambda_list)


V = 4/3 * np.pi * (d_i/2)**3
Phi = Phi_dot * V


def expressions(p):
    t_i, t_o = p
    xpr1 = Phi - (t_i - t_o) / spherical_wall_R(d_i/2, d_o/2, lambda_((t_i+t_o)/2))
    xpr2 = Phi - h * np.pi * d_o**2 * (t_o - t_f)
    return [xpr1, xpr2]


guess_values = [t_f + 20, t_f + 10]
t_i, t_o = root(expressions, guess_values).x
print(f'球罐的内表面温度为：{t_i:.2f} C')
print(f'球罐的外表面温度为：{t_o:.2f} C')
