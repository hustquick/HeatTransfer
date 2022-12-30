import numpy as np
import scipy.constants
import sys
sys.path.append("..")
from Functions.UnsteadyStateConduction import theta_to_theta_0_ratio, get_a, get_mu, get_Bi, get_Fo
import matplotlib.pyplot as plt
import os
from scipy.optimize import root
from CoolProp.CoolProp import PropsSI as psi
import scipy.constants as sc
from Functions.Self_defined import check_Fo

t_0 = 10
t_oo = -5
shape = 'S'
d = 6e-2
t_a = 5
material = 'Water'
h = 7
tau = 8*3600
t_s = 0

l_c = d/2

T_a = sc.convert_temperature(t_a, 'C', 'K')
P_a = sc.atm
rho = psi('D', 'T', T_a, 'P', P_a, material)
c = psi('C', 'T', T_a, 'P', P_a, material)
lambda_ = psi('L', 'T', T_a, 'P', P_a, material)

Bi = get_Bi(l_c, lambda_, h)
mu = get_mu(Bi, shape)
a = get_a(lambda_, rho, c)
eta = 1


def expressions(p):
    tau = p
    Fo = get_Fo(tau, l_c, a)
    ratio_s_to_0 = theta_to_theta_0_ratio(mu, eta, Fo, shape)
    xpr = t_s - t_oo - (t_0 - t_oo) * ratio_s_to_0
    return xpr


guess_values = np.ones(1)
tau = root(expressions, guess_values).x[0]
print(f'tau = {tau:.0f} s')

Fo = get_Fo(tau, l_c, a)
check_Fo(Fo)
