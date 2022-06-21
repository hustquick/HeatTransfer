from Functions.UnsteadyStateConduction import get_a, t_x_for_constant_t_w
from scipy.optimize import root
import numpy as np
from CoolProp.CoolProp import PropsSI as psi
import scipy.constants as sc
import matplotlib.pyplot as plt
import os

t_max = 48
tau_s = 10
t_w_list = np.arange(60, 110, 10)
t_0 = 37
tau_t = 5*60
material = 'Water'

T_0 = sc.convert_temperature(t_0, 'C', 'K')
rho = psi('D', 'T', T_0, 'P', sc.atm, material)
lambda_ = psi('L', 'T', T_0, 'P', sc.atm, material)
c = psi('C', 'T', T_0, 'P', sc.atm, material)
a = get_a(lambda_, rho, c)

tau = tau_t - tau_s

guess_value = 0.01
x_list = []
for t_w in t_w_list:
    x = root(lambda x: t_max - t_x_for_constant_t_w(x, tau, t_0, t_w, a),
             guess_value).x[0]
    x_list.append(x)
[print(f'当热源温度为{t_w} C, 烧伤深度为{x:.3f} m') for t_w, x in zip(t_w_list, x_list)]

t_w_lt = np.linspace(60, 110, 1000)
x_lt = []
for t_w in t_w_lt:
    x = root(lambda x: t_max - t_x_for_constant_t_w(x, tau, t_0, t_w, a),
             guess_value).x[0]
    x_lt.append(x)

fig, ax = plt.subplots()
ax.plot(t_w_lt, np.array(x_lt)*1000)
ax.set_xlabel('$t_w$/°C')
ax.set_ylabel('$x$/ mm')
name = os.path.basename(__file__).split(".")[0]
plt.savefig(f'./{name}.pdf')
plt.show()
