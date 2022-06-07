import numpy as np
from scipy.optimize import root
from Functions.UnsteadyStateConduction import theta_to_theta_0_ratio, get_a, get_mu, get_Bi, get_Fo
import matplotlib.pyplot as plt
from scipy.integrate import solve_bvp

d = 40e-2
t_0 = 600
t_oo = 30
t_surface = 450
h = 18.5
lambda_ = 22.3
a = 8.8e-6

shape = 'C'
l_c = d/2


def expressions(p):
    tau = p[0]
    Bi = get_Bi(l_c, lambda_, h)
    mu = get_mu(Bi, shape)
    eta = 1
    Fo = get_Fo(tau, l_c, a)
    xpr = t_surface - t_oo - (t_0 - t_oo) * theta_to_theta_0_ratio(mu, eta, Fo, shape)
    return xpr


guess_values = 1
tau = root(expressions, guess_values).x[0]
print(f'tau = {tau:.0f} s')
