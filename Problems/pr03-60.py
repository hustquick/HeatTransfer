import sys
sys.path.append("..")
from Functions.UnsteadyStateConduction import get_a, get_mu, get_Fo, get_Bi, t_x_for_constant_t_w, theta_to_theta_0_ratio
from scipy.optimize import root
import numpy as np
from CoolProp.CoolProp import PropsSI as psi
import scipy.constants as sc
import matplotlib.pyplot as plt
import os
from scipy.constants import hour, minute

delta = 50e-3
t_0 = 25
t_w = 1600
h = 40
a = 5e-6
lambda_ = 4.0
t_x = 1500
x = delta

guess_values = 1000
tau = root(lambda tau: t_x - t_x_for_constant_t_w(x, tau, t_0, t_w, a), guess_values).x[0]
print(f'tau = {tau:.0f} s')
