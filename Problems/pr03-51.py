import sys
sys.path.append("..")
from Functions.UnsteadyStateConduction import get_a, t_x_for_constant_t_w
from scipy.optimize import root
import numpy as np

a = 1.65e-7
t_0 = 15
t_w = -20
tau = 50*24*3600
t_x = 0

guess_value = np.ones(1)
x = root(lambda x: t_x - t_x_for_constant_t_w(x, tau, t_0, t_w, a),
         guess_value).x[0]
print(f'x = {x:.3f} m')
