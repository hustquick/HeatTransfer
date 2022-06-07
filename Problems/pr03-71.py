import numpy as np
import os
from Functions.UnsteadyStateConduction import t_x_for_constant_t_w
import matplotlib.pyplot as plt

t_0 = 20
t_w = 1450
x_list = np.linspace(0, 80e-3, 1000)
tau = 2 * 3600
a = 0.89e-6

t_list = np.zeros(len(x_list))
for i, x in enumerate(x_list):
    t = t_x_for_constant_t_w(x, tau, t_0, t_w, a)
    t_list[i] = t

fig, ax = plt.subplots()
ax.plot(x_list, t_list)
ax.set_xlabel('x (m)')
ax.set_ylabel('t (C)')
name = os.path.basename(__file__).split(".")[0]
plt.savefig(f'./{name}.pdf')
plt.show()
