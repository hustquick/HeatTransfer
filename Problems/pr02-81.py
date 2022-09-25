import scipy.constants as sc
from CoolProp.CoolProp import PropsSI as psi
from scipy.optimize import root

T_av = 470
q = 2500
t_i = 65
lambda_ = [0.047, 0.012, 0.038]
delta = [0.8e-3, 0.55e-3, 3.5e-3]
delta_12 = delta_34 = 1e-3
h_rad = 4 * sc.sigma * T_av**3


def expressions(p):
    t_2, t_4, R_total = p
    R_a = delta[0] / lambda_[0]
    R_b = delta[1] / lambda_[1]
    R_c = delta[2] / lambda_[2]
    t_1 = t_i + q * R_a
    t_12 = (t_1 + t_2)/2
    lambda_12 = psi('L', 'T', t_12, 'P', sc.atm, 'Air')
    R_12cond = delta_12 / lambda_12
    R_12 = 1 / (h_rad + 1 / R_12cond)
    xpr1 = t_2 - t_1 - q * R_12
    t_3 = t_2 + q * R_b
    t_34 = (t_3 + t_4)/2
    lambda_34 = psi('L', 'T', t_34, 'P', sc.atm, 'Air')
    R_34cond = delta_34 / lambda_34
    R_34 = 1 / (h_rad + 1 / R_34cond)
    xpr2 = t_4 - t_3 - q * R_34
    xpr3 = R_total - (R_a + R_12 + R_b + R_34 + R_c)
    return xpr1, xpr2, xpr3


guess_values = [t_i+10, t_i+20, 1]
t_2, t_4, R_total = root(expressions, guess_values).x
t_o = t_i + q * R_total
print(f'外边面的温度为：{t_o:.2f}degC')
