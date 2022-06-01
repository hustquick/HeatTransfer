from Functions.UnsteadyStateConduction import mu, \
    theta_to_theta_0_ratio, theta_to_theta_m_ratio
from scipy.constants import day
from scipy.optimize import root
import numpy as np

shape = 'P'
delta_1 = 0.5/2
delta_2 = 0.7/2
delta_3 = 1/2
lambda_ = 40.5
a = 0.722e-5
t_oo = 1200
tau = 4*3600
t_0 = 20
h = 348

Bi_1 = h * delta_1 / lambda_
Fo_1 = a * tau / delta_1**2
mu_1 = mu(Bi_1, shape)
eta_1 = 1
ratio_to_0_1 = theta_to_theta_0_ratio(mu_1, eta_1, Fo_1, shape)
ratio_to_m_1 = theta_to_theta_m_ratio(mu_1, eta_1, shape)
ratio_m_to_0_1 = ratio_to_0_1 / ratio_to_m_1


Bi_2 = h * delta_2 / lambda_
Fo_2 = a * tau / delta_2**2
mu_2 = mu(Bi_2, shape)
eta_2 = 1
ratio_to_0_2 = theta_to_theta_0_ratio(mu_2, eta_2, Fo_2, shape)
ratio_to_m_2 = theta_to_theta_m_ratio(mu_2, eta_2, shape)
ratio_m_to_0_2 = ratio_to_0_2 / ratio_to_m_2


Bi_3 = h * delta_3 / lambda_
Fo_3 = a * tau / delta_3**2
mu_3 = mu(Bi_3, shape)
eta_3 = 1
ratio_to_0_3 = theta_to_theta_0_ratio(mu_3, eta_3, Fo_3, shape)
ratio_to_m_3 = theta_to_theta_m_ratio(mu_3, eta_3, shape)
ratio_m_to_0_3 = ratio_to_0_3 / ratio_to_m_3


ratio_m_to_0 = ratio_m_to_0_1 * ratio_m_to_0_2 * ratio_m_to_0_3
t_m = t_oo + ratio_m_to_0 * (t_0 - t_oo)
print(f'最低温度为：{t_m:.2f} C')

ratio_to_0 = ratio_to_0_1 * ratio_to_0_2 * ratio_to_0_3
t = t_oo + ratio_to_0 * (t_0 - t_oo)
print(f'最高温度为：{t:.2f} C')
