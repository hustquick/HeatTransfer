import sys
sys.path.append("..")
from Functions.UnsteadyStateConduction import t_x_for_constant_q_0

q_0 = 2e4
t_0 = 20
a = 1e-7
lambda_ = 0.2
t_w_max = 180
tau = 30
x = 3e-3

t_0_tau = t_x_for_constant_q_0(0, tau, t_0, lambda_, a, q_0)
t_x_tau = t_x_for_constant_q_0(x, tau, t_0, lambda_, a, q_0)
print(f't_0_tau = {t_0_tau:.2f} C')
print(f't_x_tau = {t_x_tau:.2f} C')
