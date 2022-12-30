import numpy as np

import sys
sys.path.append("..")
from Functions.SteadyStateConduction import cylindrical_wall_R

d = 3e-3
R_e = 2.22e-3 # Ohm per meter
delta = 1e-3
lambda_ = 0.15
t_max = 65
t_min = 0

R = cylindrical_wall_R(d/2, d/2+delta, lambda_, 1)
Phi = (t_max - t_min) / R
I = np.sqrt(Phi / R_e)
print(f'I = {I:.2f} A')
