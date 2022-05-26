from CoolProp.CoolProp import PropsSI as psi
import scipy.constants as sc
import numpy as np

Delta = 0.1e-3
t_1 = 180
t_2 = 30
fluid = 'Air'
Phi = 58.2
d = 120e-3

p = sc.atm
T_1 = sc.convert_temperature(t_1, 'C', 'K')
T_2 = sc.convert_temperature(t_2, 'C', 'K')

lambda_1 = psi('L', 'T', T_1, 'P', p, fluid)
lambda_2 = psi('L', 'T', T_2, 'P', p, fluid)

area = np.pi * d**2 / 4    # 纵向单位长度的传热面积
q = Phi / area
R_total = (t_1 - t_2) / q
R_1 = Delta / lambda_1
R_2 = Delta / lambda_2
R = R_total - R_1 - R_2

error = R_total - R
error_ratio = error / R

print(f'相对误差大小为{error_ratio:.2%}')
