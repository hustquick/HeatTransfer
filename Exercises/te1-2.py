from CoolProp.CoolProp import PropsSI as psi
import scipy.constants as const

A_2 = 60e-4
p_1 = 100e3
t_1 = 25
t_2 = 47
P = 1500
fluid = 'Air'

T_1 = const.convert_temperature(t_1, 'C', 'K')
T_2 = const.convert_temperature(t_2, 'C', 'K')
h_1 = psi('H', 'T', T_1, 'P', p_1, fluid)
h_2 = psi('H', 'T', T_2, 'P', p_1, fluid)
m_dot = P / (h_2 - h_1)
rho_2 = psi('D', 'T', T_2, 'P', p_1, fluid)
q_v_2 = m_dot / rho_2
v_2 = q_v_2 / A_2
print(f"空气的质量流量为：{m_dot:.3f} kg/s，出口处的空气流速为：{v_2:.2f} m/s")
