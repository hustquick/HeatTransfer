import numpy as np

import sys
sys.path.append("..")
from Functions.SteadyStateConduction import cylindrical_wall_R

t_gas = 1000
t_water = 200
h_o = 100
h_i = 5000
delta = 6e-3
lambda_ = 42
d_o = 52e-3

delta_dirty = [0, 1e-3, 2e-3]
lamdba_dirty = [1, 0.08, 1]

d_i = d_o - 2*delta
d_o = d_o
R_1 = 1 / (h_i * np.pi * d_i)
R_2 = cylindrical_wall_R(d_i/2, d_o/2, lambda_, 1)

for i, delta_d in enumerate(delta_dirty):
    lambda_d = lamdba_dirty[i]
    R_3 = cylindrical_wall_R(d_o/2, d_o/2 + delta_d, lambda_d, 1)
    R_4 = 1 / (h_o * np.pi * (d_o + delta_d))
    R_total = R_1 + R_2 + R_3 + R_4
    q = (t_gas - t_water) / R_total
    print(f'({i+1}) q = {q:.2f} W')
