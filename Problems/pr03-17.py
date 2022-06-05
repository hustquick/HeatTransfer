import numpy as np
from scipy.optimize import root
from Functions.UnsteadyStateConduction import theta_to_theta_0_ratio, get_a, get_mu, get_Bi, get_Fo
import matplotlib.pyplot as plt

shape = 'C'
T_oo = 1e4
D_p = 50e-6
rho = 3970
lambda_ = 11
c = 1560
h = 10000
T_melt = 2350
gamma = 3580e3

T_0 = 300

l_c = D_p / 2
theta_m_to_0 = (T_melt - T_oo) / (T_0 - T_oo)
eta = 0
Bi = get_Bi(l_c, lambda_, h)
if Bi < 1/30:
    print(f'可以使用集中参数法')
    tau = - rho * c * D_p / (6 * h) * np.log(theta_m_to_0)
    print(f'加热到其熔点所需的时间为：{tau:.3e} s')
# 也可以不用集中参数法，利用下面代码直接计算：
# mu_v = mu(Bi_v, shape)
# guess_value = 1
# Fo_v = root(lambda Fo_v: theta_m_to_0 - theta_to_theta_0_ratio(mu_v, eta, Fo_v, shape), guess_value).x[0]
# guess_value2 = 1
# a_v = a(lambda_, rho, c)
# tau = root(lambda tau_v: Fo_v - Fo(tau_v, l_c, a_v), guess_value2).x[0]
# print(f'加热到其熔点所需的时间为：{tau:.3e} s')

V = 4/3 * np.pi * (D_p/2)**3
m = rho * V
Q = m * gamma
Delta_T = T_oo - T_melt
A = 4 * np.pi * (D_p/2)**2
Delta_tau = Q / (h * A * Delta_T)
print(f'从刚到达熔点直至全部熔为液滴所需的时间为：{Delta_tau:.3e} s')
