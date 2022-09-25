import numpy as np

from Functions.UnsteadyStateConduction import theta_to_theta_0_ratio, Q_to_Q_0_ratio, get_mu, get_Bi, get_Fo, get_a
import matplotlib.pyplot as plt
import os
from scipy.optimize import root
from CoolProp.CoolProp import PropsSI as psi
import scipy.constants as sc
from Functions.Self_defined import check_Fo

shape = 'S'
t_0 = -30
d = 5e-3
t_oo = 5
t_s = 0
h = 240
c = 2040
rho = 921
lambda_ = 2.56

l_c = d/2
Bi = get_Bi(l_c, lambda_, h)
mu = get_mu(Bi, shape)
a = get_a(lambda_, rho, c)


def expressions(p):
    tau = p
    Fo = get_Fo(tau, l_c, a)
    xpr = t_s - t_oo - (t_0 - t_oo) * theta_to_theta_0_ratio(mu, 1, Fo, shape)
    return xpr


guess_value = np.ones(1)
tau = root(expressions, guess_value).x[0]
print(f'tau = {tau:.0f} s')

Fo = get_Fo(tau, l_c, a)
t_m = t_oo + (t_0 - t_oo) * theta_to_theta_0_ratio(mu, 0, Fo, shape)
print(f't_m = {t_m:.2f}degC')

check_Fo(Fo)
