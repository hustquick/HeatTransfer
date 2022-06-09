import scipy.constants as sc

A = 0.2
t = 65
t_a = 25
Q = 1000

h = Q / (A * (t - t_a))
print(f'所需的对流传热系数为：{h:.2f} W/m^2-K')

t_s = 30
epsilon = 0.85
T_s = sc.convert_temperature(t_s, 'C', 'K')
T_a = sc.convert_temperature(t_a, 'C', 'K')
Q_radiation = epsilon * sc.sigma * A * (T_s**4 - T_a**4)
print(f'热辐射带走的热量为：{Q_radiation:.2f} W')
