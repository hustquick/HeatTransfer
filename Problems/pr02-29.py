import numpy as np
from scipy.optimize import root

import sys
from pathlib import Path

project_root = str(Path(__file__).resolve().parents[1])
if project_root not in sys.path:
    sys.path.insert(0, project_root)
from Functions.SteadyStateConduction import spherical_wall_R


r = 0.1e-3
t_oo = 25
lambda_ = 120
Phi = 4

R = spherical_wall_R(r, np.inf, lambda_)
guess_value = t_oo + 1
t = root(lambda t: Phi - (t - t_oo) / R, guess_value).x[0]
print(f't = {t:.2f}degC')
