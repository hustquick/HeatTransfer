import numpy as np
import scipy.constants

from Functions.UnsteadyStateConduction import theta_to_theta_0_ratio, get_a, get_mu, get_Bi, get_Fo
import matplotlib.pyplot as plt
import os
from scipy.optimize import root
from CoolProp.CoolProp import PropsSI as psi
import scipy.constants as sc
from Functions.Self_defined import check_Fo

shape = 'S'
d = 10e-2
t_0 = 250
t_oo = 10
h = 200
t_m = 150
lambda_ = 44.8
a = 1.229e-5

l_c = d/2

Bi = get_Bi(l_c, lambda_, h)
mu = get_mu(Bi, shape)
eta = 0


def expressions(p):
    tau = p
    Fo = get_Fo(tau, l_c, a)
    ratio_m_to_0 = theta_to_theta_0_ratio(mu, eta, Fo, shape)
    xpr = t_m - t_oo - (t_0 - t_oo) * ratio_m_to_0
    return xpr


guess_values = np.ones(1)
tau = root(expressions, guess_values).x[0]
print(f'tau = {tau:.0f} s')
Fo = get_Fo(tau, l_c, a)
ratio_s_to_0 = theta_to_theta_0_ratio(mu, 1, Fo, shape)
t_s = t_oo + (t_0 - t_oo) * ratio_s_to_0
print(f'T_s = {t_s:.2f} C')

check_Fo(Fo)
