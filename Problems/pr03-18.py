import numpy as np
from scipy.optimize import root
import sys
sys.path.append("..")
from Functions.UnsteadyStateConduction import theta_to_theta_0_ratio, get_a, get_mu, get_Bi, get_Fo
import matplotlib.pyplot as plt
from scipy.integrate import solve_bvp
import os
from Functions.Self_defined import find_nearest, save_pdf

d = 1e-3
t_oo = 25
R_l = 0.01
I = 120
h = 550
Delta_t = 1

c = 500
rho = 8000
lambda_ = 25

guess_values = t_oo + 1
t_balance = root(lambda t: h * np.pi * d * (t - t_oo) - I**2 * R_l, guess_values).x[0]
print(f't = {t_balance:.2f}degC')


# dt_dtau = \dfrac{I^2 R_l - \pi h d (t - t_oo)}{\pi c \rho d^2 / 4}
def derivative(x, t):
    return np.vstack((t[1], -(I**2 * R_l - h * np.pi * d * (t[0] - t_oo)) / (np.pi * c * rho * d**2 / 4)))


# 定义边界条件，t(0) = t_oo, t(np.inf) = t
# 边界条件函数的t_a和t_b参数为边界条件的起始和终止点
def bc(t_a, t_b):
    return np.array([t_a[0] - t_oo, t_b[1]])


N = 1000
tau_oo = 40
tau = np.linspace(0, tau_oo, N)
t = np.zeros((2, tau.size))
t[0, 0] = t_oo
result = solve_bvp(derivative, bc, tau, t)

x_plot = np.linspace(0, tau_oo, N)
t_plot = result.sol(x_plot)[0]
plt.plot(x_plot, t_plot)
plt.grid()
plt.xlabel(r'$\tau$/s')
plt.ylabel(r'$t/\mathrm{^\circ C}$')
name = os.path.basename(__file__).split(".")[0]
save_pdf(name, plt)

t_search = t_balance - Delta_t
arg = find_nearest(t_plot, t_search)
print(f'温度升高到{t_search:.2f}°C所需的时间为{x_plot[arg]:.1f} s')


