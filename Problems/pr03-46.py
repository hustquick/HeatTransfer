import numpy as np
import scipy.constants
import sys
sys.path.append("..")
from Functions.UnsteadyStateConduction import theta_to_theta_0_ratio, Q_to_Q_0_ratio, get_mu, get_Bi, get_Fo, get_a
import matplotlib.pyplot as plt
import os
from scipy.optimize import root
from CoolProp.CoolProp import PropsSI as psi
import scipy.constants as sc
from Functions.Self_defined import check_Fo

shape = 'S'
T_0 = 600
T_oo = 300
d_A = 200e-3
d_B = 20e-3
rho_A = 1600
rho_B = 400
c_A = 0.4e3
c_B = 1.6e3
lambda_A = 170
lambda_B = 1.7
h_A = 5
h_B = 50
T = 415

l_c_A = d_A / 2
l_c_B = d_B / 2

Bi_A = get_Bi(l_c_A, lambda_A, h_A)
Bi_B = get_Bi(l_c_B, lambda_B, h_B)
mu_A = get_mu(Bi_A, shape)
mu_B = get_mu(Bi_B, shape)
a_A = get_a(lambda_A, rho_A, c_A)
a_B = get_a(lambda_B, rho_B, c_B)


def expressions(p):
    tau_As, tau_Bs, tau_Am, tau_Bm = p
    Fo_As = get_Fo(tau_As, l_c_A, a_A)
    Fo_Bs = get_Fo(tau_Bs, l_c_B, a_B)
    Fo_Am = get_Fo(tau_Am, l_c_A, a_A)
    Fo_Bm = get_Fo(tau_Bm, l_c_B, a_B)
    ratio_As_to_0 = theta_to_theta_0_ratio(mu_A, 1, Fo_As, shape)
    xpr1 = T - T_oo - (T_0 - T_oo) * ratio_As_to_0
    ratio_Bs_to_0 = theta_to_theta_0_ratio(mu_B, 1, Fo_Bs, shape)
    xpr2 = T - T_oo - (T_0 - T_oo) * ratio_Bs_to_0
    ratio_Am_to_0 = theta_to_theta_0_ratio(mu_A, 0, Fo_Am, shape)
    xpr3 = T - T_oo - (T_0 - T_oo) * ratio_Am_to_0
    ratio_Bm_to_0 = theta_to_theta_0_ratio(mu_B, 0, Fo_Bm, shape)
    xpr4 = T - T_oo - (T_0 - T_oo) * ratio_Bm_to_0
    return xpr1, xpr2, xpr3, xpr4


guess_values = np.ones(4)
tau_As, tau_Bs, tau_Am, tau_Bm = root(expressions, guess_values).x
print(f'A球表面冷却到{T} K所需的时间为{tau_As:.0f} s')
print(f'B球表面冷却到{T} K所需的时间为{tau_Bs:.0f} s')
print(f'A球中心冷却到{T} K所需的时间为{tau_Am:.0f} s')
print(f'B球中心冷却到{T} K所需的时间为{tau_Bm:.0f} s')

Fo_As = get_Fo(tau_As, l_c_A, a_A)
Fo_Bs = get_Fo(tau_Bs, l_c_B, a_B)
Fo_Am = get_Fo(tau_Am, l_c_A, a_A)
Fo_Bm = get_Fo(tau_Bm, l_c_B, a_B)

check_Fo(Fo_As, Fo_Bs, Fo_Am, Fo_Bm)
