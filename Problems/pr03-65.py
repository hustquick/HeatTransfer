from scipy.optimize import root
import numpy as np
from CoolProp.CoolProp import PropsSI as psi
import scipy.constants as sc
import matplotlib.pyplot as plt
import os
from scipy.constants import hour, minute

import sys
sys.path.append("..")
from Functions.UnsteadyStateConduction import get_a, get_mu, get_Fo, get_Bi, t_x_for_constant_t_w, theta_to_theta_0_ratio
from Functions.Self_defined import check_Fo

shape = 'S'
d = 60e-3
t_0 = 350
t_oo = 280
lambda_ = 1.6
a = 7e-7

l_c = d/2

Q_m_to_0 = 0.9
theta_m_to_0 = 1 - Q_m_to_0
mu = get_mu(l_c, shape)


def expressions(p):
    tau = p
    Fo = get_Fo(tau, l_c, a)
    xpr = theta_m_to_0 - theta_to_theta_0_ratio(mu, 0, Fo, shape)
    return xpr


guess_values = np.ones(1)
tau = root(expressions, guess_values).x[0]
print(f'tau = {tau:.0f} s')

Fo = get_Fo(tau, l_c, a)
check_Fo(Fo)
