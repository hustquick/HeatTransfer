from Functions.UnsteadyStateConduction import tau_c, Bi, Fo
import numpy as np

length = 20e-3
d = 4e-3
h = 11.63
tau = 5 * 60
c = 0.138e3
rho = 13110
lambda_ = 10.36

r = d/2
V = np.pi * r**2 * length
A = np.pi * r**2 + np.pi * d * length
l_c = V / A
Bi = Bi(l_c, lambda_, h)
if Bi < 0.05:
    print(f'可以使用集中参数法')

    tau_c = tau_c(l_c, rho, c, h)
    Fo = Fo(l_c, rho, c, lambda_, tau)
    Delta_T_ratio = np.exp(- Bi * Fo)
    print(f'5分钟后，温度计读数的过余温度为初始过余温度的{Delta_T_ratio:.2%}')
