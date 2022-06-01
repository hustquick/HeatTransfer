from Functions.UnsteadyStateConduction import tau_c, Bi
import numpy as np

d = 5e-2
t_0 = 450
t_oo = 30
h = 24
t = 300
c = 0.48e3
rho = 7753
lambda_ = 33

l_c = d / 6
Bi = Bi(l_c, lambda_, h)
if Bi < 1/30:
    print(f'可以使用集中参数法')

    tau_c = tau_c(l_c, rho, c, h)
    Delta_T_ratio = (t - t_oo) / (t_0 - t_oo)
    tau = - tau_c * np.log(Delta_T_ratio)
    print(f'tau = {tau:.0f} s')
