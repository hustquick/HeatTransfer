from Functions.UnsteadyStateConduction import get_a, t_x_for_constant_t_w
from scipy.optimize import root
import numpy as np
from CoolProp.CoolProp import PropsSI as psi
import scipy.constants as sc
import matplotlib.pyplot as plt
import os

t_w = 70
t_0 = 25
delta = 6e-3
x = 2e-3
t_x = 30
a = 4e-7

guess_value = np.ones(1)
tau = root(lambda tau: t_x - t_x_for_constant_t_w(x, tau, t_0, t_w, a),
           guess_value).x[0]
print(f'tau = {tau:.1f} s')
