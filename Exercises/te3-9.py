import numpy as np
import matplotlib.pyplot as plt

c = 2.094e3
t_0 = 20
t_oo = 320
h_list = np.array([58, 116])
tau_c_list = c / h_list
theta_0 = t_0 - t_oo
tau = np.linspace(0, 4*max(tau_c_list), 1000)
fig, ax = plt.subplots()
for tau_c in tau_c_list:
    theta = theta_0 * np.exp(-tau/tau_c)
    ax.plot(tau, theta, label=rf'$\tau_c = {tau_c:.2f}$ s')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$\theta$')
ax.legend()
plt.savefig('te3-9.pdf')
plt.show()

