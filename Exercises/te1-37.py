import numpy as np
from CoolProp.CoolProp import PropsSI as psi
import scipy.constants as sc

A_out = 3
t_out = 0
epsilon = 0.05
t_a = -100

T_out = sc.convert_temperature(t_out, 'C', 'K')
T_a = sc.convert_temperature(t_a, 'C', 'K')

Q = epsilon * sc.sigma * A_out * (T_out**4 - T_a**4)
print(f'模拟仓表面的辐射散热量为：{Q:.2f} W')
print(f'这份能量不都是宇航员身上散失的，还有部分是舱内仪表散失的')
