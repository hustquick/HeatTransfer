import numpy as np
from scipy.optimize import root

t_0 = 25
t_oo = 200
tau_c = 1
h = 350
lambda_ = 20
c = 400
rho = 8500


def expression(p):
    d = p
    V = 4/3 * np.pi * (d/2)**3
    A = 4 * np.pi * (d/2)**2
    xpr = tau_c - rho * c * V / (h * A)
    return xpr


guess_value = 1
d = root(expression, guess_value).x[0]
print(f'd = {d:.2e} m')
print('如果考虑气流与热接点之间的辐射换热，则h增大，则V/A增大，d增大')
