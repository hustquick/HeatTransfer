import numpy as np
from scipy.optimize import root
from Functions.UnsteadyStateConduction import theta_to_theta_0_ratio, get_a, get_mu, get_Bi, get_Fo
import matplotlib.pyplot as plt
from scipy.integrate import solve_bvp
from Functions.Self_defined import check_Fo

t_0 = 1000
t_oo = 5
h = 1135
tau = 5*60
delta = 50e-3
lambda_ = 56.8
a = 4.13e-6

# 由于内侧面绝热，该问题可以等效为无限大平板，l_c = delta
l_c = delta
shape = 'P'
Bi = get_Bi(l_c, lambda_, h)
mu = get_mu(Bi, shape)
Fo = get_Fo(tau, l_c, a)
t_delta = t_oo + (t_0 - t_oo) * theta_to_theta_0_ratio(mu, 1, Fo, shape)
t_m = t_oo + (t_0 - t_oo) * theta_to_theta_0_ratio(mu, 0, Fo, shape)
print(f'表面温度为 {t_delta:.2f} C')
print(f'内侧温度为 {t_m:.2f} C')

check_Fo(Fo)
