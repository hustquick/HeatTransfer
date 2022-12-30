import numpy as np
import sys
sys.path.append("..")
from Functions.UnsteadyStateConduction import get_Bi, get_tau_c, get_a

carbon_percentage = 0.5e-2
t_0 = 600
t_oo = 20
m = 7.84
area = 870e-4
c = 418.7
rho = 7840
h = 29.1
Delta_t = 10
t = t_oo + Delta_t

lambda_ = 49.8

V = m / rho
l_c = V / area
Bi = get_Bi(l_c, lambda_, h)
if Bi < 0.1:
    print(f'可以使用集中参数法')
    theta_m_to_theta_0 = (t - t_oo) / (t_0 - t_oo)
    a = get_a(lambda_, rho, c)
    tau_c = get_tau_c(l_c, lambda_, a, h)
    tau = -tau_c * np.log(theta_m_to_theta_0)
    print(f'所需时间为：{tau:.0f} s')
