import numpy as np
from Functions.UnsteadyStateConduction import theta_to_theta_0_ratio, get_a, get_mu, get_Bi, get_Fo
import matplotlib.pyplot as plt
import os

d = 500e-3
height = 800e-3
t_0 = 30
t_oo = 1200
h = 180
lambda_ = 40
a = 8e-6
tau = 3*3600
x = 400e-3
r = 0.13
shape = ['P', 'C']

# 先考虑厚度方向，作为无限大平板进行分析
l_c_1 = height / 2
Bi_1 = h * l_c_1 / lambda_
Fo_1 = get_Fo(tau, l_c_1, a)
mu_1 = get_mu(Bi_1, shape[0])
eta_1 = 0
ratio_m_to_0_1 = theta_to_theta_0_ratio(mu_1, eta_1, Fo_1, shape[0])
if np.any([Fo_1]) <= 0.2:
    print('Fo数不满足上述公式的要求，上述结果不可靠！')

# 再考虑径向，作为无限长圆柱进行分析
l_c_2 = d / 2
Bi_2 = get_Bi(l_c_2, lambda_, h)
Fo_2 = get_Fo(tau, l_c_2, a)
mu_2 = get_mu(Bi_2, shape[1])
eta_2 = 0
ratio_m_to_0_2 = theta_to_theta_0_ratio(mu_2, eta_2, Fo_2, shape[1])
if np.any([Fo_1]) <= 0.2:
    print('Fo数不满足上述公式的要求，上述结果不可靠！')

ratio_m_to_0 = ratio_m_to_0_1 * ratio_m_to_0_2
t_m = t_oo + ratio_m_to_0 * (t_0 - t_oo)
print(f't_m = {t_m:.2f} C')
