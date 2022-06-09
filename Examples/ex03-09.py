from Functions.UnsteadyStateConduction import get_mu, \
    theta_to_theta_0_ratio
import numpy as np
from Functions.Self_defined import check_Fo

shape = ['P', 'C']
d = 600e-3
l = 1000e-3
t_0 = 30
t_oo = 1300
tau = 4*3600
h = 232
lambda_ = 40.5
a = 0.625e-5

# 先考虑厚度方向，作为无限大平板进行分析
l_c_1 = l / 2
Bi_1 = h * l_c_1 / lambda_
Fo_1 = a * tau / l_c_1**2
mu_1 = get_mu(Bi_1, shape[0])
eta_1 = 0
ratio_m_to_0_1 = theta_to_theta_0_ratio(mu_1, eta_1, Fo_1, shape[0])

# 再考虑径向，作为无限长圆柱进行分析
l_c_2 = d / 2
Bi_2 = h * l_c_2 / lambda_
Fo_2 = a * tau / l_c_2**2
mu_2 = get_mu(Bi_2, shape[1])
eta_2 = 0
ratio_m_to_0_2 = theta_to_theta_0_ratio(mu_2, eta_2, Fo_2, shape[1])

ratio_m_to_0 = ratio_m_to_0_1 * ratio_m_to_0_2
t_m = t_oo + ratio_m_to_0 * (t_0 - t_oo)
print(f't_m = {t_m:.2f} C')

Fo = [Fo_1, Fo_2]
check_Fo(Fo)
