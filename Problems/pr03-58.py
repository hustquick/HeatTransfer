from Functions.UnsteadyStateConduction import get_a, get_mu, get_Fo, get_Bi, t_x_for_constant_t_w, theta_to_theta_0_ratio
from scipy.optimize import root
import numpy as np
from CoolProp.CoolProp import PropsSI as psi
import scipy.constants as sc
import matplotlib.pyplot as plt
import os
from scipy.constants import hour, minute
from Functions.Self_defined import check_Fo

d = 10e-2
height = 10e-2
shape = ['P', 'C']
t_0 = 260
t_oo = 30
h = 250
tau = 3*60
lambda_ = 47.5
a = 9.55e-6

l_c_1 = height/2
l_c_2 = d/2

Bi_1 = get_Bi(l_c_1, lambda_, h)
Bi_2 = get_Bi(l_c_2, lambda_, h)
mu_1 = get_mu(Bi_1, shape[0])
mu_2 = get_mu(Bi_2, shape[1])
Fo_1 = get_Fo(tau, l_c_1, a)
Fo_2 = get_Fo(tau, l_c_2, a)
ratio_m_to_0_1 = theta_to_theta_0_ratio(mu_1, 0, Fo_1, shape[0])
ratio_m_to_0_2 = theta_to_theta_0_ratio(mu_2, 0, Fo_2, shape[1])
ratio_m_to_0 = ratio_m_to_0_1 * ratio_m_to_0_2
t_m = t_oo + (t_0 - t_oo) * ratio_m_to_0
ratio_s_to_0_1 = theta_to_theta_0_ratio(mu_1, 1, Fo_1, shape[0])
ratio_s_to_0_2 = theta_to_theta_0_ratio(mu_2, 1, Fo_2, shape[1])
ratio_s_to_0 = ratio_s_to_0_1 * ratio_s_to_0_2
t_s = t_oo + (t_0 - t_oo) * ratio_s_to_0
Delta_t = t_m - t_s
print(f'Delta_t = {Delta_t:.0f}degC')

check_Fo(Fo_1, Fo_2)
