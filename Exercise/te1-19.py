import scipy.constants as sc

a = b = 10e-3
t_s = 20
t_max = 85
h = 175
delta = 1e-3

epsilon = 0.9

A = a * b + 2 * delta * a + 2 * delta * b
T_max = sc.convert_temperature(t_max, 'C', 'K')
T_s = sc.convert_temperature(t_s, 'C', 'K')
Q_conv = h * A * (T_max - T_s)
Q_radi = epsilon * sc.sigma * A * (T_max ** 4 - T_s**4)
Q = Q_conv + Q_radi
print(f'芯片的最大允许功率为：{Q:.2f} W')
