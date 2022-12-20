import numpy as np
import matplotlib.pyplot as plt
import os
from Functions.Self_defined import save_pdf

c = 2.094e3
t_0 = 20
t_oo = 320
h_list = np.array([58, 116])
tau_c_list = c / h_list
print(f'两种情况下，热电偶的时间常数分别为:{tau_c_list[0]:.2f} s和 {tau_c_list[1]:.2f} s')
theta_0 = t_0 - t_oo
tau = np.linspace(0, 4*max(tau_c_list), 1000)
fig, ax = plt.subplots()
for tau_c in tau_c_list:
    theta = theta_0 * np.exp(-tau/tau_c)
    ax.plot(tau, theta, label=rf'$\tau_c = {tau_c:.2f}$ s')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$\theta$')
ax.legend()
name = os.path.basename(__file__).split(".")[0]
save_pdf(name, plt)
