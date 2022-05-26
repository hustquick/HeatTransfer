import numpy as np
from CoolProp.CoolProp import PropsSI as psi
from scipy.optimize import root
import scipy.constants as sc

delta_g = 3e-3
delta_air = 6e-3
lambda_g = 0.8
t_i = 15
t_o = -10

air_pressure = sc.atm


def expressions(p):
    t_12, t_23, t_34, t_45, q, lambda_air1, lambda_air2 = p
    xpr1 = q - (t_i - t_12) * lambda_g / delta_g
    xpr2 = q - (t_12 - t_23) * lambda_air1 / delta_air
    xpr3 = q - (t_23 - t_34) * lambda_g / delta_g
    xpr4 = q - (t_34 - t_45) * lambda_air2 / delta_air
    xpr5 = q - (t_45 - t_o) * lambda_g / delta_g
    xpr6 = lambda_air1 - psi('L', 'T', sc.convert_temperature(((t_12 + t_23) / 2), 'C', 'K'), 'P', air_pressure, 'Air')
    xpr7 = lambda_air2 - psi('L', 'T', sc.convert_temperature(((t_34 + t_45) / 2), 'C', 'K'), 'P', air_pressure, 'Air')
    return [xpr1, xpr2, xpr3, xpr4, xpr5, xpr6, xpr7]

guess_value = [t_i- 1, t_i-2, t_i-3, t_i-4, 1, lambda_g, lambda_g]
t_12, t_23, t_34, t_45, q, lambda_air1, lambda_air2 = root(expressions, guess_value).x
print(f'q = {q:.2f} W/m^2')
