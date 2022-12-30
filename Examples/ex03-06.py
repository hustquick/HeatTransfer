import sys
sys.path.append("..")
from Functions.UnsteadyStateConduction import t_x_for_constant_t_w

t_0 = 20
t_w = 1450
x = 80e-3
tau = 2 * 3600
a = 0.89e-6

t = t_x_for_constant_t_w(x, tau, t_0, t_w, a)
print(f't = {t:.2f} C')
