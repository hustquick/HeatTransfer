import numpy as np
import scipy.constants

from Functions.UnsteadyStateConduction import theta_to_theta_0_ratio, get_a, get_mu, get_Bi, get_Fo
import matplotlib.pyplot as plt
import os
from scipy.optimize import root
from CoolProp.CoolProp import PropsSI as psi
import scipy.constants as sc

shape = 'S'
T_x = 1000
T_oo = 1300
h = 5000
d = 20e-3
T_0 = 300
delta = 1e-3
x = d/2 - delta
rho = 7800
c = 500
lambda_ = 50

l_c = d/2

Bi = get_Bi(l_c, lambda_, h)
mu = get_mu(Bi, shape)
a = get_a(lambda_, rho, c)
eta = x / l_c


def expressions(p):
    tau = p
    Fo = get_Fo(tau, l_c, a)
    ratio_x_to_0 = theta_to_theta_0_ratio(mu, eta, Fo, shape)
    xpr = T_x - T_oo - (T_0 - T_oo) * ratio_x_to_0
    return xpr


guess_values = np.ones(1)
tau = root(expressions, guess_values).x[0]
print(f'tau = {tau:.1f} s')

Fo = get_Fo(tau, l_c, a)

if np.any([Fo]) <= 0.2:
    print('Fo数不满足上述公式的要求，上述结果不可靠！')
