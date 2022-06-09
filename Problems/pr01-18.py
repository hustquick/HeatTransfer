import scipy.constants as sc

T_a = 2.7
T = 250
epsilon = 0.7
q = epsilon * sc.sigma * (T ** 4 - T_a ** 4)
print(f'航天器单位表面积的换热量为：{q:.2f} W/m^2')
