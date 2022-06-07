import numpy as np
import scipy.constants

from Functions.UnsteadyStateConduction import theta_to_theta_0_ratio, get_a, get_mu, get_Bi, get_Fo
import matplotlib.pyplot as plt
import os
from scipy.optimize import root
from CoolProp.CoolProp import PropsSI as psi
import scipy.constants as sc

shape = 'S'
t_oo = 250
d = 5e-2
t_0 = 20

t_a = 50
material = 'water'

tau = 20*60
h = 20

T_a = sc.convert_temperature(t_a, 'C', 'K')
P_a = sc.atm
rho = psi('D', 'T', T_a, 'P', P_a, material)
c = psi('C', 'T', T_a, 'P', P_a, material)
lambda_ = psi('L', 'T', T_a, 'P', P_a, material)

l_c = d/2

Bi = get_Bi(l_c, lambda_, h)
a = get_a(lambda_, rho, c)
mu = get_mu(Bi, shape)
eta = 1
Fo = get_Fo(tau, l_c, a)
ratio_s_to_0 = theta_to_theta_0_ratio(mu, eta, Fo, shape)
t = t_oo + (t_0 - t_oo) * ratio_s_to_0

print(f't = {t:.2f} C')

if np.any([Fo]) <= 0.2:
    print('Fo数不满足上述公式的要求，上述结果不可靠！')
