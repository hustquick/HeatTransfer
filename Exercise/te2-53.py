from functions import fin_tip_Delta_T_ratio
import numpy as np
from scipy.optimize import root

D = 127e-3
d = 15e-3
delta = 0.9e-3
lambda_ = 49.1
h = 105
Delta_T_ratio = 0.6e-2

perimeter = np.pi * d
A_c = np.pi * (d/2 + delta)**2 - np.pi * (d/2)**2

guess_value = 0.1
H = root(lambda H: Delta_T_ratio - fin_tip_Delta_T_ratio(H, perimeter, A_c, lambda_, h), guess_value).x[0]
print(f'套管应有的长度为：{H:.3f} m')
