import numpy as np
from Functions.UnsteadyStateConduction import theta_to_theta_0_ratio, get_a, get_mu, get_Bi, get_Fo
import matplotlib.pyplot as plt
import os
from Functions.Self_defined import check_Fo

t_0 = 30
t_oo = 1400
d = 600e-3
tau_list = np.arange(2, 6) * 3600
lambda_ = 43.5
a = 7.5e-6
h = 290

shape = 'C'
l_c = d/2
t_s_list = np.zeros(len(tau_list))
t_m_list = np.zeros(len(tau_list))
for i, tau in enumerate(tau_list):
    Bi = get_Bi(l_c, lambda_, h)
    mu = get_mu(Bi, shape)
    Fo = get_Fo(tau, l_c, a)
    t_s = t_oo + (t_0 - t_oo) * theta_to_theta_0_ratio(mu, 1, Fo, shape)
    t_s_list[i] = t_s
    t_m = t_oo + (t_0 - t_oo) * theta_to_theta_0_ratio(mu, 0, Fo, shape)
    t_m_list[i] = t_m
    print(f'{int(tau/3600)}小时后: t_s = {t_s:.2f} C, t_m = {t_m:.2f} C')

tau = np.linspace(2*3600, 5*3600, 100000)
Bi = get_Bi(l_c, lambda_, h)
mu = get_mu(Bi, shape)
Fo = get_Fo(tau, l_c, a)
t_s = t_oo + (t_0 - t_oo) * theta_to_theta_0_ratio(mu, 1, Fo, shape)
t_m = t_oo + (t_0 - t_oo) * theta_to_theta_0_ratio(mu, 0, Fo, shape)

fig, ax = plt.subplots()
ax.plot(tau, t_s, label='$t_s$')
ax.plot(tau, t_m, label='$t_m$')
ax.set_xlabel(r'$\tau$ (s)')
ax.set_ylabel('$t$ (°C)')
plt.legend()
name = os.path.basename(__file__).split(".")[0]
plt.savefig(f'./{name}.pdf')
plt.show()

check_Fo(*Fo)  # 由于Fo是数组，需要对其解包
