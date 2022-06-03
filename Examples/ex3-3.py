from Functions.UnsteadyStateConduction import tau_c, Bi, a
import numpy as np

d = 5e-2
l = 30e-2
t_0 = 30
t_oo = 1200
t = 800
h = 140
c = 0.48e3
rho = 7753
lambda_ = 33

r = d / 2
V = np.pi * r**2 * l
A = 2 * np.pi * r**2 + np.pi * d * l
l_c = V / A
Bi = Bi(l_c, lambda_, h)

if Bi < 0.05:
    print(f'可以使用集中参数法')
    Delta_T_ratio = (t - t_oo) / (t_0 - t_oo)
    a = a(lambda_, rho, c)
    tau_c = tau_c(l_c, lambda_, a, h)
    tau = - tau_c * np.log(Delta_T_ratio)
    print(f'tau = {tau:.0f} s')
