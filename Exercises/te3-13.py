import numpy as np
from scipy.optimize import root
from Functions.UnsteadyStateConduction import t_x_for_constant_h, Bi, tau_c, Fo
import matplotlib.pyplot as plt

delta = 20e-3
t_0 = 500
t_oo = 20
h = 35
lambda_ = 45
a = 1.37e-5
Delta_t = 10
t = t_oo + Delta_t

l_c = delta / 2
Bi = Bi(l_c, lambda_, h)
if Bi < 0.1:
    print(f'可以使用集中参数法')


    def expressions(p):
        tau = p
        tau_c = lambda_ * l_c / (h * a)
        Delta_T_ratio = np.exp(- tau / tau_c)
        xpr = Delta_T_ratio - Delta_t / (t_0 - t_oo)
        return xpr


    guess_value = 1
    tau = root(expressions, guess_value).x[0]
    print(f'所需时间为：{tau:.0f} s')
