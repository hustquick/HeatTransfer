import numpy as np
from scipy.optimize import root
from Functions.UnsteadyStateConduction import theta_to_theta_0_ratio, get_a, get_mu, get_Bi, get_Fo
import matplotlib.pyplot as plt
from scipy.integrate import solve_bvp

delta = 300e-3
t_0 = 20
t_oo = 1200
a = 5.55e-6
h = 290
Delta_t = 15
lambda_ = 49.8
shape = 'P'

t_surface = t_oo - Delta_t

l_c = delta
Bi = get_Bi(l_c, lambda_, h)
mu = get_mu(Bi, shape)


def expressions(p):
    tau = p
    Fo = get_Fo(tau, l_c, a)
    xpr = t_surface - t_oo - (t_0 - t_oo) * theta_to_theta_0_ratio(mu, 1, Fo, shape)
    return xpr


guess_value = [1]
tau = root(expressions, guess_value).x[0]
print(f'tau = {tau:.0f} s')

Fo = get_Fo(tau, l_c, a)
t_m = t_oo + (t_0 - t_oo) * theta_to_theta_0_ratio(mu, 0, Fo, shape)
Delta_t_tau = t_surface - t_m
print(f'此时钢板两表面的温差为{Delta_t_tau:.0f} C')
