import numpy as np

t = 500
lambda_ = 210
rho = 7200
c = 420
t_0 = 25
t_oo = 650
tau = 1*60
h = 12

# 先假设满足集中参数法，后续再验证Bi数满足条件
theta_m_to_theta_0 = (t - t_oo) / (t_0 - t_oo)
tau_c = -tau / np.log(theta_m_to_theta_0)
d = 4 * h *tau_c / (rho * c)
print(f'导线的直径应限制在{d*1000:.2f} mm以下')
Bi = h * d / (4*lambda_)
if Bi < 0.1:
    print(f'前面假设的集中参数法适用')
else:
    print(f'前面假设的集中参数法不适用')
