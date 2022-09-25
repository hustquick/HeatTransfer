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
r = 0.15
t_0 = 30
lambda_ = 0.8
c = 840
rho = 2750
t_oo = 410
h = 10.5
tau = 8*3600

l_c = r

Bi = get_Bi(l_c, lambda_, h)
mu = get_mu(Bi, shape)
a = get_a(lambda_, rho, c)
eta = 1
Fo = get_Fo(tau, l_c, a)
ratio_s_to_0 = theta_to_theta_0_ratio(mu, eta, Fo, shape)
t_s = t_oo + (t_0 - t_oo) * ratio_s_to_0
print(f't_s = {t_s:.0f}degC')

check_Fo(Fo)
