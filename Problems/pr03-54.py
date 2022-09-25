from Functions.UnsteadyStateConduction import get_a, get_mu, get_Fo, get_Bi, t_x_for_constant_t_w, theta_to_theta_0_ratio
from scipy.optimize import root
import numpy as np
from CoolProp.CoolProp import PropsSI as psi
import scipy.constants as sc
import matplotlib.pyplot as plt
import os
from Functions.Self_defined import check_Fo

t_0 = 25
t_oo = 425
shape = 'P'
h = 6.5
tau = 4 * sc.hour + 50 * sc.minute + 24
length = 0.1
rho = 810
c = 2550
lambda_ = 0.65
l_c = length/2


a = get_a(lambda_, rho, c)
Bi = get_Bi(l_c, lambda_, h)
mu = get_mu(Bi, shape)
eta = 1
Fo = get_Fo(tau, l_c, a)
ratio_s_to_0 = theta_to_theta_0_ratio(mu, eta, Fo, shape)
ratio = ratio_s_to_0**3
t = t_oo + (t_0 - t_oo) * ratio
print(f't = {t:.2f}degC')

check_Fo(Fo)
