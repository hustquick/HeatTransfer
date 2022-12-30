import numpy as np
import sys
sys.path.append("..")
from Functions.UnsteadyStateConduction import theta_to_theta_0_ratio, get_a, get_mu, get_Bi, get_Fo
import matplotlib.pyplot as plt
import os
from Functions.Self_defined import check_Fo

d = 30e-3
lambda_ = 0.3
rhoc = 1050e3
t = 200
tau = 3*60
t_oo = 150
h = 8.5
shape = 'C'

l_c = d/2

Bi = get_Bi(l_c, lambda_, h)
a = lambda_ / rhoc
mu = get_mu(Bi, shape)
eta = 1
Fo = get_Fo(tau, l_c, a)
ratio_m_to_0 = theta_to_theta_0_ratio(mu, eta, Fo, shape)
t_0 = t_oo + (t - t_oo) / ratio_m_to_0
print(f't_0 = {t_0:.2f}degC')

check_Fo(Fo)
