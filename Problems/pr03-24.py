import numpy as np
from scipy.optimize import root
from Functions.UnsteadyStateConduction import theta_to_theta_0_ratio, get_a, get_mu, get_Bi, get_Fo
import matplotlib.pyplot as plt
from scipy.integrate import solve_bvp

H = 0.4
h = 50
lambda_ = 20
a = 5.6e-6

# 由于圆柱侧面绝热，该问题可以等效为无限大平板，l_c = H/2
shape = 'P'
l_c = H/2
Bi = get_Bi(l_c, lambda_, h)
mu = get_mu(Bi, shape)
eta = 0


def expressions(p):
    tau = p
    Fo = get_Fo(tau, l_c, a)
    xpr = theta_to_theta_0_ratio(mu, eta, Fo, shape) - 0.5
    return xpr


guess_values = 100000
tau = root(expressions, guess_values).x[0]
print(f'圆桂体中心过余温度下降到初值一半所需要的时间为{tau:.0f} s')

Fo = get_Fo(tau, l_c, a)
if np.any([Fo]) <= 0.2:
    print('Fo数不满足上述公式的要求，上述结果不可靠！')
