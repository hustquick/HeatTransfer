from Functions.SteadyStateConduction import fin_tip_R
import numpy as np
from scipy.optimize import root

t_w = 70
l_1, l_2 = 10e-2, 16e-2
H, d = 3e-2, 4.2e-2
lambda_ = 15
t_f = 20
h = 70
Phi = 80

perimeter = np.pi * d
A_c = np.pi * d**2 / 4
H_p = H + d/4  # H_p = H + A_c/perimeter
R_fin = fin_tip_R(H_p, perimeter, A_c, lambda_, h)


def expressions(p):
    number = p
    R_fins = R_fin / number
    R_base = 1 / (h * (l_1*l_2 - number*np.pi*d**2/4))
    xpr = Phi - (t_w - t_f) * (1/R_base + 1/R_fins)
    return xpr


guess_values = 1
number = root(expressions, guess_values).x[0]
print(f'需要{int(np.ceil(number))}个针肋')
