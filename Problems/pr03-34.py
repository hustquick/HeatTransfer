import numpy as np
from scipy.optimize import root
import sys
sys.path.append("..")
from Functions.UnsteadyStateConduction import theta_to_theta_0_ratio, get_a, get_mu, get_Bi, get_Fo
import matplotlib.pyplot as plt
from scipy.integrate import solve_bvp
from Functions.Self_defined import check_Fo

d = 170e-3
t_0 = 17
t_oo = 850
lambda_ = 30
a = 6.2e-6
h = 141

t_m = 800

shape = 'C'
l_c = d/2


def expressions(p):
    tau = p[0]
    Bi = get_Bi(l_c, lambda_, h)
    mu = get_mu(Bi, shape)
    eta = 0
    Fo = get_Fo(tau, l_c, a)
    xpr = t_m - t_oo - (t_0 - t_oo) * theta_to_theta_0_ratio(mu, eta, Fo, shape)
    return xpr


guess_values = 1
tau = root(expressions, guess_values).x[0]
print(f'tau = {tau:.0f} s')

Fo = get_Fo(tau, l_c, a)
check_Fo(Fo)
