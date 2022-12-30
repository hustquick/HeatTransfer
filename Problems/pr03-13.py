import numpy as np
import sys
sys.path.append("..")
from Functions.UnsteadyStateConduction import get_Bi, get_tau_c

delta = 20e-3
t_0 = 500
t_oo = 20
h = 35
lambda_ = 45
a = 1.37e-5
Delta_t = 10
t = t_oo + Delta_t

l_c = delta / 2
Bi = get_Bi(l_c, lambda_, h)
if Bi < 0.1:
    print(f'可以使用集中参数法')

    theta_m_to_theta_0 = (t - t_oo) / (t_0 - t_oo)
    tau_c = get_tau_c(l_c, lambda_, a, h)
    tau = -tau_c * np.log(theta_m_to_theta_0)
    print(f'所需时间为：{tau:.0f} s')
