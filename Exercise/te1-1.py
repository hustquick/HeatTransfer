import scipy.constants as const
from CoolProp.CoolProp import PropsSI as psi

t = 20
P = 150
l = 5
w = 3
h = 2.5
tau = 10 * 3600
fluid = 'Air'

T = const.convert_temperature(t, 'C', 'K')
p = const.atm
rho = psi('D', 'T', T, 'P', p, fluid)
V = l * w * h
m = rho * V
Q = P * tau
h_1 = psi('H', 'T', T, 'P', p, fluid)
H_1 = m * h_1
H_2 = H_1 + Q
h_2 = H_2 / m
T_2 = psi('T', 'H', h_2, 'P', p, fluid)
t_2 = const.convert_temperature(T_2, 'K', 'C')
