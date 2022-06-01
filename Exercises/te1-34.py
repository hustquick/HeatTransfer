from CoolProp.CoolProp import PropsSI as psi
import scipy.constants as sc

fluid1 = 'R22'
fluid2 = 'Air'
T_f = 313
T_a = 283
A_air = 0.4
v_air = 2
q_m = 0.011
h = 40

gamma = psi('H', 'T', T_f, 'Q', 1, fluid1) - psi('H', 'T', T_f, 'Q', 0, fluid1)
Q = q_m * gamma
h_in_air = psi('H', 'T', T_a, 'P', sc.atm, fluid2)
density_air = psi('D', 'T', T_a, 'P', sc.atm, fluid2)
m_dot_air = v_air * A_air * density_air
h_out_air = Q / m_dot_air + h_in_air
T_out_air = psi('T', 'H', h_out_air, 'P', sc.atm, fluid2)
T_air_average = (T_out_air + T_a) / 2
A = Q / h / (T_f - T_air_average)
print(f"所需的传热面积为：{A:.2f} m^2")
