from Functions.UnsteadyStateConduction import get_mu, \
    theta_to_theta_0_ratio
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
mu_1 = get_mu(Bi_1, shape)
ratio_w_to_0_1 = theta_to_theta_0_ratio(mu_1, 1, Fo_1, shape)
ratio_m_to_0_1 = theta_to_theta_0_ratio(mu_1, 0, Fo_1, shape)


Bi_2 = h * delta_2 / lambda_
Fo_2 = a * tau / delta_2**2
mu_2 = get_mu(Bi_2, shape)
ratio_w_to_0_2 = theta_to_theta_0_ratio(mu_2, 1, Fo_2, shape)
ratio_m_to_0_2 = theta_to_theta_0_ratio(mu_2, 0, Fo_2, shape)


Bi_3 = h * delta_3 / lambda_
Fo_3 = a * tau / delta_3**2
mu_3 = get_mu(Bi_3, shape)
ratio_w_to_0_3 = theta_to_theta_0_ratio(mu_3, 1, Fo_3, shape)
ratio_m_to_0_3 = theta_to_theta_0_ratio(mu_3, 0, Fo_3, shape)


ratio_m_to_0 = ratio_m_to_0_1 * ratio_m_to_0_2 * ratio_m_to_0_3
t_m = t_oo + ratio_m_to_0 * (t_0 - t_oo)
print(f'最低温度为：{t_m:.2f} C')

ratio_w_to_0 = ratio_w_to_0_1 * ratio_w_to_0_2 * ratio_w_to_0_3
t = t_oo + ratio_w_to_0 * (t_0 - t_oo)
print(f'最高温度为：{t:.2f} C')

Fo = [Fo_1, Fo_2, Fo_3]
if np.any([Fo]) <= 0.2:
    print('Fo数不满足上述公式的要求，上述结果不可靠！')
