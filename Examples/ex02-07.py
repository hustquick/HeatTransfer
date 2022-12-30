import sys
sys.path.append("..")
from Functions.SteadyStateConduction import fin_tip_efficiency2
import numpy as np

d = 25e-3
H = 15e-3
delta = 1.0e-3
t_0 = 170
t_f = 25
lambda_ = 200
h = 130

H_p = H + delta / 2
r_1 = d / 2
r_2 = d / 2 + H_p
A_L = delta * H_p

eta = fin_tip_efficiency2(H_p, A_L, lambda_, h)

A_f = 2 * np.pi * (r_2**2 - r_1**2)
Phi_0 = h * A_f * (t_0 - t_f)
Phi = eta * Phi_0
print(f'Phi = {Phi:.2f} W')

length = 0.94
N = 300
distance = 3e-3
l_bare = 20e-3

A_r = np.pi * d * (distance - delta) * N
A_f_N = A_f * N
A_0 = A_f_N + A_r + 2 * np.pi * d * l_bare
eta_0 = (A_r + eta * A_f_N) / A_0
Phi_overall = A_0 * eta_0 * h * (t_0 - t_f)
print(f'总换热量为 {Phi_overall:.2f} W')
