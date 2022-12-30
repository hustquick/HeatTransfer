import sys
sys.path.append("..")
from Functions.UnsteadyStateConduction import get_a, get_tau_c, get_Bi, get_Fo
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
Bi = get_Bi(l_c, lambda_, h)
if Bi < 0.05:
    print('可以使用集中参数法')
    a = get_a(lambda_, rho, c)
    tau_c = get_tau_c(l_c, lambda_, a, h)
    Fo = get_Fo(tau, l_c, a)
    Delta_T_ratio = np.exp(- Bi * Fo)
    print(f'5分钟后，温度计读数的过余温度为初始过余温度的{Delta_T_ratio:.2%}')
