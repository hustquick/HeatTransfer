import scipy.constants as const

t = 25
h = 2.6
t_s = 30
epsilon = 0.95
t_summer = 26
t_winter = 10

d = 25e-2
height = 1.75

T_s = const.convert_temperature(t_s, 'C', 'K')
T_summer = const.convert_temperature(t_summer, 'C', 'K')
T_winter = const.convert_temperature(t_winter, 'C', 'K')

A = const.pi * d * height + const.pi * d ** 2 / 4
q_conv = h * A * (t_s - t)
q_radi_summer = epsilon * const.sigma * A * (T_s**4 - T_summer**4)
q_summer = q_conv + q_radi_summer
q_radi_winter = epsilon * const.sigma * A * (T_s**4 - T_winter**4)
q_winter = q_conv + q_radi_winter
