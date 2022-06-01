import numpy as np
from Functions.SteadyStateConduction import fin_tip_efficiency2, cylindrical_wall_R
from scipy.optimize import root

delta = 15e-3
d_i = 120e-3
d_o = 140e-3
d_f = 250e-3
lambda_ = 45
t_i = 300
t_f = 20
h = 10

H_p = (d_f - d_o)/2 + delta
A_L = 2 * H_p * delta
efficiency = fin_tip_efficiency2(H_p, A_L, lambda_, h)
r_1 = d_o / 2
r_2 = d_o / 2 + H_p
area = 2 * np.pi * (r_2**2 - r_1**2)

R_tube = cylindrical_wall_R(d_i/2, d_o/2, lambda_, 2*delta)


def expressions(p):
    # 传热热阻可以看成管道导热热阻和法兰对热传热热阻的串联，流经管道和法兰的热流量相等
    Phi, t_o = p
    xpr1 = Phi - efficiency * h * area * (t_o - t_f)
    xpr2 = Phi - (t_i - t_o) / R_tube
    return xpr1, xpr2


guess_values = [1, t_i - 10]
Phi, t_o = root(expressions, guess_values).x
print(f'Phi = {Phi:.2f} W')
