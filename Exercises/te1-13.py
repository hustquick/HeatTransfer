import numpy as np
from CoolProp.CoolProp import PropsSI as psi
import scipy.constants as sc

p = 1.013e5
P = 50
d = 4e-3
l = 10e-2
t_s = 109
fluid = 'Water'

T = psi('T', 'P', p, 'Q', 0, fluid)
t = sc.convert_temperature(T, 'K', 'C')


A = np.pi * d * l
h = P / (A * (t_s - t))
print(f'对流传热表面传热系数为：{h:.2f} W/(m^2-K)')
