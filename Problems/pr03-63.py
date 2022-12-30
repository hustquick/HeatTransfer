import sys
sys.path.append("..")
from Functions.UnsteadyStateConduction import get_a, get_mu, get_Fo, get_Bi, t_x_for_constant_t_w, theta_to_theta_0_ratio
from scipy.optimize import root
import numpy as np
from CoolProp.CoolProp import PropsSI as psi
import scipy.constants as sc
import matplotlib.pyplot as plt
import os
from scipy.constants import hour, minute
from Functions.Self_defined import check_Fo

shape = 'S'
d = 10e-3
t_0 = 450
t_oo_1 = 25
t_m_1 = 350
h_1 = 10
t_oo_2 = 25
t_m_2 = 50
h_2 = 6000
rho = 3200
c = 1200
lambda_ = 18

l_c = d/2
a = get_a(lambda_, rho, c)
Bi_1 = get_Bi(l_c, lambda_, h_1)
mu_1 = get_mu(Bi_1, shape)


def expressions(p):
    tau_1 = p
    Fo_1 = get_Fo(tau_1, l_c, a)
    ratio_m_to_0_1 = theta_to_theta_0_ratio(mu_1, 0, Fo_1, shape)
    xpr = ratio_m_to_0_1 - (t_m_1 - t_oo_1) / (t_0 - t_oo_2)
    return xpr


guess_values = np.ones(1)
tau_1 = root(expressions, guess_values).x[0]
print(f'tau_1 = {tau_1:.0f} s')
Fo_1 = get_Fo(tau_1, l_c, a)
check_Fo(Fo_1)
ratio_m_to_0_1 = theta_to_theta_0_ratio(mu_1, 0, Fo_1, shape)
V = 4/3* np.pi * (d/2)**3
Q_0 = V * rho * c * (t_0 - t_oo_1)
Q_1 = (1 - ratio_m_to_0_1) * Q_0
print(f'Q_1 = {Q_1:.0f} J')
if Bi_1 < 0.1/3:
    print(f'可以用集中参数法，认为小球的内部的温度均匀一致。')
    t_0_2 = t_m_1

    Bi_2 = get_Bi(l_c, lambda_, h_2)
    mu_2 = get_mu(Bi_2, shape)


    def expressions2(p):
        tau_2 = p
        Fo_2 = get_Fo(tau_2, l_c, a)
        ratio_m_to_0_2 = theta_to_theta_0_ratio(mu_2, 0, Fo_2, shape)
        xpr = ratio_m_to_0_2 - (t_m_2 - t_oo_2) / (t_0_2 - t_oo_2)
        return xpr


    guess_values2 = np.ones(1)
    tau_2 = root(expressions2, guess_values2).x[0]
    print(f'tau_2 = {tau_2:.0f} s')
    Fo_2 = get_Fo(tau_2, l_c, a)
    check_Fo(Fo_2)
    ratio_m_to_0_2 = theta_to_theta_0_ratio(mu_2, 0, Fo_2, shape)
    Q_0_2 = V * rho * c * (t_0_2 - t_oo_2)
    Q_2 = (1 - ratio_m_to_0_2) * Q_0_2
    print(f'Q_2 = {Q_2:.0f} J')
