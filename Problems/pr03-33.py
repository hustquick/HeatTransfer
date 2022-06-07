import numpy as np
from scipy.optimize import root
from Functions.UnsteadyStateConduction import theta_to_theta_0_ratio, get_a, get_mu, get_Bi, get_Fo
import matplotlib.pyplot as plt
from scipy.integrate import solve_bvp

d = 20e-2
t_0 = 20
t_oo = 100
tau = 10*60
t_m = 80
rho = 8440
c = 377
lambda_ = 109

shape = 'C'
l_c = d/2


def expressions(p):
    h = p[0]
    Bi = get_Bi(l_c, lambda_, h)
    mu = get_mu(Bi, shape)
    eta = 0
    a = get_a(lambda_, rho, c)
    Fo = get_Fo(tau, l_c, a)
    xpr = t_m - t_oo - (t_0 - t_oo) * theta_to_theta_0_ratio(mu, eta, Fo, shape)
    return xpr


guess_values = 1
h = root(expressions, guess_values).x[0]
print(f'h = {h:.2f} W/m^2-K')

a = get_a(lambda_, rho, c)
Fo = get_Fo(tau, l_c, a)
if np.any([Fo]) <= 0.2:
    print('Fo数不满足上述公式的要求，上述结果不可靠！')
