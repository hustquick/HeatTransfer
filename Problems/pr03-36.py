import numpy as np
import sys
sys.path.append("..")
from Functions.UnsteadyStateConduction import theta_to_theta_0_ratio, get_a, get_mu, get_Bi, get_Fo
import matplotlib.pyplot as plt
import os
from Functions.Self_defined import check_Fo, save_pdf

t_0 = 30
t_oo = 1400
d = 600e-3
tau_list = np.arange(2, 6) * 3600
lambda_ = 43.5
a = 7.5e-6
h = 290

shape = 'C'
l_c = d/2
t_s_list = []
t_m_list = []
for tau in tau_list:
    Bi = get_Bi(l_c, lambda_, h)
    mu = get_mu(Bi, shape)
    Fo = get_Fo(tau, l_c, a)
    t_s = t_oo + (t_0 - t_oo) * theta_to_theta_0_ratio(mu, 1, Fo, shape)
    t_s_list.append(t_s)
    t_m = t_oo + (t_0 - t_oo) * theta_to_theta_0_ratio(mu, 0, Fo, shape)
    t_m_list.append(t_m)
    print(f'{int(tau/3600)}小时后: t_s = {t_s:.2f}degC, t_m = {t_m:.2f}degC')

tau = np.linspace(2*3600, 5*3600, 100000)
Bi = get_Bi(l_c, lambda_, h)
mu = get_mu(Bi, shape)
Fo = get_Fo(tau, l_c, a)
t_s = t_oo + (t_0 - t_oo) * theta_to_theta_0_ratio(mu, 1, Fo, shape)
t_m = t_oo + (t_0 - t_oo) * theta_to_theta_0_ratio(mu, 0, Fo, shape)

fig, ax = plt.subplots()
ax.plot(tau, t_s, label='$t_s$')
ax.plot(tau, t_m, label='$t_m$')
ax.set_xlabel(r'$\tau$/s')
ax.set_ylabel('$t/\mathrm{^\circ C}$')
plt.legend()
name = os.path.basename(__file__).split(".")[0]
save_pdf(name, plt)

map(check_Fo, Fo)  # 由于Fo是容器，需要使用map函数对容器中的每个元素调用check_Fo函数
