import sys
sys.path.append("..")
from Functions.UnsteadyStateConduction import t_x_for_constant_t_w
from scipy.optimize import root, minimize
import numpy as np
from math import erf
from CoolProp.CoolProp import PropsSI as psi
import scipy.constants as sc

t_0 = 25
t_w = 50
x = np.array([0.01, 0.1, 1.0, 10])
delta_t = 0.1
a = 1e-5
t = t_0 + delta_t

theta_ratio = (t - t_w) / (t_0 - t_w)
eta = root(lambda eta: theta_ratio - erf(eta), 1).x[0]
tau = (x/2/eta)**2/a

for i, tau_ in enumerate(tau):
    print(f'({i+1}) tau = {tau_:.0f} s')
