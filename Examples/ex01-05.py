import scipy.constants as sc

t = 25
h = 2.6
t_s = 30
epsilon = 0.95
t_summer = 26
t_winter = 10

d = 25e-2
height = 1.75

T_s = sc.convert_temperature(t_s, 'C', 'K')
T_summer = sc.convert_temperature(t_summer, 'C', 'K')
T_winter = sc.convert_temperature(t_winter, 'C', 'K')

A = sc.pi * d * height + sc.pi * d ** 2 / 4
q_conv = h * A * (t_s - t)
q_radi_summer = epsilon * sc.sigma * A * (T_s ** 4 - T_summer ** 4)
q_summer = q_conv + q_radi_summer
print(f'夏天时，人与环境的换热量为：{q_summer:.2f} W')
q_radi_winter = epsilon * sc.sigma * A * (T_s ** 4 - T_winter ** 4)
q_winter = q_conv + q_radi_winter
print(f'冬天时，人与环境的换热量为：{q_winter:.2f} W')
