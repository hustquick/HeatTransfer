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

d = 1
delta = 45e-3
t_0 = -20
t_oo = 80
h = 400
lambda_ = 43
a = 1.17e-5

tau = 5*60
shape = 'P'
l_c = delta

Bi = get_Bi(l_c, lambda_, h)
mu = get_mu(Bi, shape)
Fo = get_Fo(tau, l_c, a)
ratio_m_to_0 = theta_to_theta_0_ratio(mu, 0, Fo, shape)
t_m = t_oo + (t_0 - t_oo) * ratio_m_to_0
print(f't_m = {t_m:.2f}degC')
ratio_s_to_0 = theta_to_theta_0_ratio(mu, 1, Fo, shape)
t_s = t_oo + (t_0 - t_oo) * ratio_s_to_0
q = h*(t_oo - t_s)
print(f'q = {q:.0f} W/m^2')
Q_ratio_m_to_0 = 1 - ratio_m_to_0
r_1 = d/2
r_2 = d/2 - delta
# rho * c = lambda_ / a
Q_0 = np.pi * (r_1**2 - r_2**2) * lambda_ / a * (t_oo - t_0)
Q = Q_0 * Q_ratio_m_to_0
print(f'Q = {Q:.0f} W/m')
