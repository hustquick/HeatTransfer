import sys
sys.path.append("..")
from Appendix.Appendix4_lambda_ import get_lambda_
from CoolProp.CoolProp import PropsSI as psi
import scipy.constants as sc
from scipy.optimize import root

delta_1 = 1e-3
lambda_1 = 160
delta_4 = 2e-3
lambda_4 = 200
delta_3 = 10e-3
material_3 = '超细玻璃棉毡、管'
delta_2 = 20e-3
material_2 = 'Air'

t_01 = 20
t_45 = -30


def expressions(p):
    t_12, t_23, t_34, q = p
    lambda_3 = get_lambda_(material_3, (t_23 + t_34) / 2)
    lambda_2 = psi('L', 'T', sc.convert_temperature((t_12 + t_23) / 2, 'C', 'K'), 'P', sc.atm, material_2)
    expr1 = q - (t_01 - t_12) * lambda_1 / delta_1
    expr2 = q - (t_12 - t_23) * lambda_2 / delta_2
    expr3 = q - (t_23 - t_34) * lambda_3 / delta_3
    expr4 = q - (t_34 - t_45) * lambda_4 / delta_4
    return expr1, expr2, expr3, expr4


guess_value = [t_01 - 1, t_01 - 2, t_01 - 3, 1]
t_12, t_23, t_34, q = root(expressions, guess_value).x
lambda_3 = get_lambda_(material_3, (t_23 + t_34) / 2)
lambda_2 = psi('L', 'T', sc.convert_temperature((t_12 + t_23) / 2, 'C', 'K'), 'P', sc.atm, material_2)
print(f'每平方米上的散热量是：{q:.2f} W/m^2')

# 如果散热量降到一半
q_p = q / 2


def expressions2(p):
    t_12p, t_23p, t_34p, delta_3p = p
    lambda_3p = get_lambda_(material_3, (t_23p + t_34p) / 2)
    lambda_2p = psi('L', 'T', sc.convert_temperature((t_12p + t_23p) / 2, 'C', 'K'), 'P', sc.atm, material_2)
    expr1 = q_p - (t_01 - t_12p) * lambda_1 / delta_1
    expr2 = q_p - (t_12p - t_23p) * lambda_2p / delta_2
    expr3 = q_p - (t_23p - t_34p) * lambda_3p / delta_3p
    expr4 = q_p - (t_34p - t_45) * lambda_4 / delta_4
    return expr1, expr2, expr3, expr4


guess_value = [t_12, t_23, t_34, delta_3]
t_12p, t_23p, t_34p, delta_3p = root(expressions2, guess_value).x
lambda_3p = get_lambda_(material_3, (t_23p + t_34p) / 2)
lambda_2p = psi('L', 'T', sc.convert_temperature((t_12p + t_23p) / 2, 'C', 'K'), 'P', sc.atm, material_2)
print(f'保温层应增加到：{delta_3p * 1000:.0f} mm')
