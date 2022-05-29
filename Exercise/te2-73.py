import numpy as np
from scipy.optimize import root

a = 10e-3
b = 10e-3
delta_3 = 0.02e-3
R_12c = 0.9e-4   # m^2-K/W
t_oo = 25
h = 150
q = 1.5e4   # W/m^2
lambda_3 = 236

R_1 = 1 / (h * a * b)
R_12 = R_12c / (a * b)
R_3 = delta_3 / (lambda_3 * a * b)
R_34 = 1 / (h * a * b)


def expressions(p):
    t = p[0]
    Phi_1 = (t - t_oo) / R_1
    Phi_2 = (t - t_oo) / (R_12 + R_3 + R_34)
    xpr = q * a * b - Phi_1 - Phi_2
    return xpr


guess_values = np.array([t_oo + 10])
t = root(expressions, guess_values).x[0]
print(f'芯片的工作温度为：{t:.2f} C')
