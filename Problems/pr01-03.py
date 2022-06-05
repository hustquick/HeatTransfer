import scipy.constants as sc
from CoolProp.CoolProp import PropsSI as psi

fluid = 'Water'
q_v = 1000e-6/60
t_0 = 15
t_1 = 43
t_2 = 38
t_3 = 27
tau = 15*60

T_0, T_1, T_2, T_3 = sc.convert_temperature([t_0, t_1, t_2, t_3], 'C', 'K')
p = sc.atm
rho = psi('D', 'T', T_1, 'P', p, fluid)
q_m = q_v*rho
h_1 = psi('H', 'T', T_1, 'P', p, fluid)
h_0 = psi('H', 'T', T_0, 'P', p, fluid)
Q_1 = q_m*(h_1-h_0)
h_3 = psi('H', 'T', T_3, 'P', p, fluid)
Q_2 = q_m*(h_1-h_3)
ratio = (Q_1 - Q_2)/Q_1
saved_energy = q_m*(h_1 - h_3) * tau
print(f'可以节省{saved_energy:.2f}J, 约为{saved_energy/(sc.hour * sc.kilo):.2f}度电')
