import numpy as np
from Functions.UnsteadyStateConduction import theta_to_theta_0_ratio, get_a, get_mu, get_Bi, get_Fo
import matplotlib.pyplot as plt
import os
from scipy.optimize import root

d = 25e-3
shape = 'C'
R_l = 0.10
T_0 = 800
T_oo = 300
h = 120
T_m = 500
rho = 2600
c = 808
lambda_ = 3.98

l_c = d/2

h_p = 1 / (1/h + R_l*np.pi*d)
Bi = get_Bi(l_c, lambda_, h_p)
a = get_a(lambda_, rho, c)
mu = get_mu(Bi, shape)
eta = 0


def expressions(p):
    tau = p
    Fo = get_Fo(tau, l_c, a)
    ratio_m_to_0 = theta_to_theta_0_ratio(mu, eta, Fo, shape)
    xpr = ratio_m_to_0 - (T_m - T_oo) / (T_0 - T_oo)
    return xpr


guess_values = np.ones(1)
tau = root(expressions, guess_values).x[0]
print(f'Tau = {tau:.0f} s')

Fo = get_Fo(tau, l_c, a)
if np.any([Fo]) <= 0.2:
    print('Fo数不满足上述公式的要求，上述结果不可靠！')
