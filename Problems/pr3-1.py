import numpy as np
from scipy.optimize import root
import matplotlib.pyplot as plt
from Functions.UnsteadyStateConduction import t_x_for_constant_t_w

delta = 30e-3
t_0 = 20
t_w = 60
t_m = 56
a_list = np.array([170e-6, 103e-6, 12.9e-6, 0.59e-6, 0.155e-6])

guess_value = 1
tau_list = np.zeros(len(a_list))
for i, a in enumerate(a_list):
    x = delta / 2
    tau = root(lambda tau: t_x_for_constant_t_w(x, tau, t_0, t_w, a) - t_m, guess_value).x[0]
    tau_list[i] = tau
print(f'所需时间分别为：')
for tau in tau_list:
    print(f'{tau:.0f} s')
