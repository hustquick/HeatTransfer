import numpy as np

d = 7.5e-3
distance = 10e-3
t_f = 25
t_w = 120
W = 10e-2


def h(u):
    return 5.12 * u**0.65 / d**0.35


u_list = np.array([0.6, 1.0, 1.5, 2.0, 2.5])
h_list = h(u_list)
