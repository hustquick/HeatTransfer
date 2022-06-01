import numpy as np
from Functions.SteadyStateConduction import spherical_wall_R
from scipy.optimize import root

r = 0.1e-3
t_oo = 25
lambda_ = 120
Phi = 4

R = spherical_wall_R(r, np.inf, lambda_)
guess_value = t_oo + 1
t = root(lambda t: Phi - (t - t_oo) / R, guess_value).x[0]
print(f't = {t:.2f} C')
