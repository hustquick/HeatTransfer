import numpy as np
from scipy.optimize import root
from Functions.UnsteadyStateConduction import theta_to_theta_0_ratio, get_a, get_mu, get_Bi, get_Fo
import matplotlib.pyplot as plt
from scipy.integrate import solve_bvp

delta = 3e-2/2
t_0 = 150
t_w = 30
a = 2e-6


def theta_ratio(delta, x, tau, number_to_calculate):
    sum = 0
    for n in range(1, number_to_calculate+1):
        # 课本上的公式有误
        sum += 1/n * np.exp(-(n*np.pi/(2*delta))**2 * a*tau) * np.sin(n * np.pi * x / (2*delta))
    return 4/np.pi * sum


tau = 1*60

result1 = theta_ratio(delta, delta, tau, 1)
print(f'取一项的结果为：theta_ratio = {result1:.6f}')
result2 = theta_ratio(delta, delta, tau, 4)
print(f'取四项的结果为：theta_ratio = {result2:.6f}')
t_m = t_w + result1 * (t_0 - t_w)
print(f't_m = {t_m:.2f}degC')
