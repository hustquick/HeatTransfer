import numpy as np

import sys
sys.path.append("..")
from Functions.SteadyStateConduction import spherical_wall_R

r_1 = 10e-3
r_2 = 12.5e-3
r_3 = 16.3e-3
t_fi = 37
t_fo = 20
h_i = 12
h_o = 6
lambda_1 = 0.35
lambda_2 = 0.8
ratio = 1/3

area_1 = ratio * 4 * np.pi * r_1**2
area_2 = ratio * 4 * np.pi * r_2**2
area_3 = ratio * 4 * np.pi * r_3**2

R_i = 1 / (h_i * area_1)
# 由于球面可看做各部分热阻并联组成，所以热阻等于球壳的热阻除以ratio
R_1 = spherical_wall_R(r_1, r_2, lambda_1) / ratio
R_2 = spherical_wall_R(r_2, r_3, lambda_2) / ratio
R_o = 1 / (h_o * area_2)
R_o_p = 1 / (h_o * area_3)

R_total = R_i + R_1 + R_o
R_total_p = R_i + R_1 + R_2 + R_o_p

Phi = (t_fi - t_fo) / R_total
Phi_p = (t_fi - t_fo) / R_total_p

print(f'Phi = {Phi:.3f} W')
print(f'Phi_p = {Phi_p:.3f} W')
