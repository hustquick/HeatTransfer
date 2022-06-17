from Functions.UnsteadyStateConduction import get_a, get_mu, get_Fo, get_Bi, t_x_for_constant_t_w, theta_to_theta_0_ratio
from scipy.optimize import root
import numpy as np
from CoolProp.CoolProp import PropsSI as psi
import scipy.constants as sc
import matplotlib.pyplot as plt
import os
from scipy.constants import hour, minute
from Functions.Self_defined import check_Fo

d = 0.15
height = 0.05
t_0 = 30
t_oo = 450
h = 9.5
t_m = 400
shape = ['P', 'C']
l_c_1 = height/2
l_c_2 = d/2

lambda_ = 0.78
rho = 2700
c = 835

a = get_a(lambda_, rho, c)
Bi_1 = get_Bi(l_c_1, lambda_, h)
Bi_2 = get_Bi(l_c_2, lambda_, h)
mu_1 = get_mu(Bi_1, shape[0])
mu_2 = get_mu(Bi_2, shape[1])
eta_1 = 0
eta_2 = 0


def expressions(p):
    tau = p
    Fo_1 = get_Fo(tau, l_c_1, a)
    ratio_m_to_0_1 = theta_to_theta_0_ratio(mu_1, eta_1, Fo_1, shape[0])
    Fo_2 = get_Fo(tau, l_c_2, a)
    ratio_m_to_0_2 = theta_to_theta_0_ratio(mu_2, eta_2, Fo_2, shape[1])
    ratio_m_to_0 = ratio_m_to_0_1 * ratio_m_to_0_2
    xpr = ratio_m_to_0 - (t_m - t_oo) / (t_0 - t_oo)
    return xpr


guess_values = np.ones(1)
tau = root(expressions, guess_values).x[0]
print(f'tau = {tau:.0f} s')

Fo_1 = get_Fo(tau, l_c_1, a)
Fo_2 = get_Fo(tau, l_c_2, a)
check_Fo(Fo_1, Fo_2)
