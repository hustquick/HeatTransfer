import numpy as np
from scipy.optimize import root
import sys
sys.path.append("..")
from Functions.UnsteadyStateConduction import theta_to_theta_0_ratio, get_a, get_mu, get_Bi, get_Fo
import matplotlib.pyplot as plt
from scipy.integrate import solve_bvp
from Functions.Self_defined import check_Fo

delta = 8e-3
t_0 = -15
t_oo = 25
h = 4.4
t_m = 10
lambda_ = 1.1
a = 7.5e-7

# 该问题可以等效为无限大平板，l_c = delta/2
l_c = delta/2
shape = 'P'

Bi = get_Bi(l_c, lambda_, h)
mu = get_mu(Bi, shape)
eta = 0


def expressions(p):
    tau = p[0]
    Fo = get_Fo(tau, l_c, a)
    xpr = (t_m - t_oo) / (t_0 - t_oo) - theta_to_theta_0_ratio(mu, eta, Fo, shape)
    return xpr


guess_values = 1
tau = root(expressions, guess_values, method='lm').x[0]
print(f'tau = {tau:.0f} s')

Fo = get_Fo(tau, l_c, a)
check_Fo(Fo)

l_c_1 = delta

Bi_1 = get_Bi(l_c_1, lambda_, h)
mu_1 = get_mu(Bi_1, shape)
eta_1 = 0


def expressions(p):
    tau = p[0]
    Fo_1 = get_Fo(tau, l_c_1, a)
    xpr = (t_m - t_oo) / (t_0 - t_oo) - theta_to_theta_0_ratio(mu_1, eta_1, Fo_1, shape)
    return xpr


guess_values = 1
tau_1 = root(expressions, guess_values, method='lm').x[0]
print(f'tau_1 = {tau_1:.0f} s')

Fo_1 = get_Fo(tau, l_c_1, a)
check_Fo(Fo_1)
