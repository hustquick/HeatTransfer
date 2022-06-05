from Appendix import Appendix5_air_physical_properties as ap5
import numpy as np

delta_1 = delta_2 = 6e-3
delta_air = 8e-3
t_in = 20
t_out = -20
width = length = 60e-2
lambda_ = 0.78

t = (t_in + t_out) / 2
lambda_air = np.interp(t, ap5.temperature_list, ap5.lambda_list)
# 也可以利用CoolProp计算lambda的值
# lambda_air2 = psi('L', 'T', t+273.15, 'P', 101325, 'Air')

area = width * length
R_1 = delta_1 / (lambda_ * area)
R_2 = delta_2 / (lambda_ * area)
R_air = delta_air / (lambda_air * area)

R = R_1 + R_2 + R_air
q = (t_in - t_out) / R
print(f'热损失为{q:.2f} W')

R_p = delta_1 / (lambda_ * area)
q_p = (t_in - t_out) / R_p
times = q_p / q
print(f'其热损失是双层玻璃的{times:.2f}倍')
