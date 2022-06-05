from scipy.optimize import root
from CoolProp.CoolProp import PropsSI as psi
import scipy.constants as sc

t_i = 20
t_o = 5
h_i = 7
h_o = 28
delta_1 = 12e-3
lambda_1 = 0.16
delta_2 = 25e-3
lambda_2u = 0.141
l_2u = 75e-3
l_2d = 330e-3
fluid_2d = 'Air'
delta_3 = 200e-3
lambda_3 = 0.72


def expressions(p):
    t_12, t_23, Phi = p
    T_12 = sc.convert_temperature(t_12, 'C', 'K')
    T_23 = sc.convert_temperature(t_23, 'C', 'K')
    lambda_2d = psi('L', 'T', (T_12 + T_23)/2, 'P', sc.atm, fluid_2d)

    height = l_2u + l_2d
    area = height # 单位长度面积
    R_i = 1 / (h_i * area)
    R_1 = delta_1 / (lambda_1 * area)
    R_2u = delta_2 / (lambda_2u * l_2u)
    R_2d = delta_2 / (lambda_2d * l_2d)
    R_2 = 1 / (1/R_2u + 1/R_2d)
    R_3 = delta_3 / (lambda_3 * area)
    R_o = 1 / (h_o * area)

    R_total = R_i + R_1 + R_2 + R_3 + R_o
    # print(R_i*area, R_1*area, R_2*area, R_3*area, R_o*area, R_total*area)
    xpr1 = Phi - (t_i - t_o) / R_total
    xpr2 = t_i - t_12 - Phi * (R_i + R_1)
    xpr3 = t_i - t_23 - Phi * (R_i + R_1 + R_2)
    return [xpr1, xpr2, xpr3]


guess_values = [t_i - 1, t_i - 2, 1]
t_1, t_2, Phi = root(expressions, guess_values).x
print(f'Phi = {Phi:.2f} W')
