import numpy as np

from Functions.UnsteadyStateConduction import t_x_for_constant_t_w, get_mu, get_Bi, get_Fo, get_a
import matplotlib.pyplot as plt
import os
from scipy.optimize import root
from CoolProp.CoolProp import PropsSI as psi
import scipy.constants as sc

t_0 = 30
t_w = 100
x = 10e-3
tau = 2*60
t_x = 65
rho = 2200
c = 700


def expressions(p):
    lambda_ = p
    a = get_a(lambda_, rho, c)
    xpr = t_x - t_x_for_constant_t_w(x, tau, t_0, t_w, a)
    return xpr


guess_value = np.ones(1)
lambda_ = root(expressions, guess_value).x[0]
print(f'lambda = {lambda_:.2f} W/m-K$')
