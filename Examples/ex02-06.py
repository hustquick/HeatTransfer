import sys
sys.path.append("..")
from Functions.SteadyStateConduction import fin_tip_Delta_T_ratio
import numpy as np
from scipy.optimize import root

t_show = 100
t_0 = 50
H = 140e-3
delta = 1e-3
lambda_ = 58.2
h = 29.1

ratio = fin_tip_Delta_T_ratio(H, np.pi*1, np.pi*1*delta, lambda_, h)
guess_value = t_0 + 10
t_f = root(lambda t_f: ratio - (t_f - t_show) / (t_f - t_0), guess_value).x[0]
print(f't_f = {t_f:.2f} C')
