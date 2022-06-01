import numpy as np
from CoolProp.CoolProp import PropsSI as psi
import scipy.constants as sc
from scipy.integrate import quad
from scipy.optimize import root
import sympy as sp

print('该男子向环境散热的方式有对流和辐射')

epsilon = 0.9
t_initial = 31
t_amb = 10
h = 20
d = 0.318
height = 1.7

T_initial = sc.convert_temperature(t_initial, 'C', 'K')
T_amb = sc.convert_temperature(t_amb, 'C', 'K')
A = np.pi * d**2 / 4 + np.pi * d * height

Phi_1 = 400
# Phi_2 = 800
C = 5e5
tau = 1 * sc.hour

# Phi = Phi_2 - Phi_1
# Delta_T = Phi / C * tau
# T_final = T_initial - Delta_T

T, Q_rad, Q_conv = sp.Symbol('T'), sp.Symbol('Q_rad'), sp.Symbol('Q_conv')
Q_rad = epsilon * sc.sigma * A * (T**4 - T_amb**4)
Q_conv = h * A * (T - T_amb)
dQ_dtau = Q_rad + Q_conv - Phi_1
dQ_dT = C
dtau_dT = dQ_dT / dQ_dtau

dQrad_dT = sp.lambdify(T, -Q_rad * dtau_dT, 'numpy')
dQconv_dT = sp.lambdify(T, -Q_conv * dtau_dT, 'numpy')


def expressions(p):
    Q_rad_total, Q_conv_total, T_final = p
    exp1 = Q_rad_total - quad(dQrad_dT, T_initial, T_final)[0]
    exp2 = Q_conv_total - quad(dQconv_dT, T_initial, T_final)[0]
    exp3 = (Q_rad_total + Q_conv_total - Phi_1 * tau) - C * (T_initial - T_final)
    return [exp1, exp2, exp3]
# Q_rad_total = sp.integrate(-Q_rad * dtau_dT, (T, T_initial, T_final))
# Q_conv_total = sp.integrate(-Q_conv * dtau_dT, (T, T_initial, T_final))


guess_value = [1e6, 1e6, T_initial - 4]
Q_rad_total, Q_conv_total, T_final = root(expressions, guess_value).x

print(f'辐射总换热量为： {Q_rad_total:.4e} J')
print(f'对流总换热量为： {Q_conv_total:.4e} J')
