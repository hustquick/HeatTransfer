import numpy as np
from scipy.optimize import root
from Functions.UnsteadyStateConduction import t_x_for_constant_h, get_a, get_mu, get_Bi, get_Fo, theta_to_theta_0_ratio
import matplotlib.pyplot as plt
from scipy.integrate import solve_bvp
from Functions.Self_defined import check_Fo

l_1 = 10e-2
l_2 = 5e-2
t_0 = 20
t_oo = 200
h = 125
tau = 6*60
rho = 7820
c = 460
lambda_ = 15.2

# 其他面绝热，因此可将问题简化为厚度为2*l_2的对称无限大平板处理
l_c = l_2
x = 0
shape = 'P'

a = get_a(lambda_, rho, c)
Bi = get_Bi(l_c, lambda_, h)
mu = get_mu(Bi, shape)
Fo = get_Fo(tau, l_c, a)
eta = x / l_c
ratio_m_to_0 = theta_to_theta_0_ratio(mu, eta, Fo, shape)
t = t_oo + ratio_m_to_0 * (t_0 - t_oo)
print(f't = {t:.2f}degC')

check_Fo(Fo)
