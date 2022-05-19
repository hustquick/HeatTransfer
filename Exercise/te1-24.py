t_w1 = 460
t_f2 = 300
delta_1 = 5e-3
delta_2 = 0.5e-3
lambda_1 = 46.5
lambda_2 = 1.16
h_2 = 5800

R_1 = delta_1 / lambda_1
R_2 = delta_2 / lambda_2
R_3 = 1 / h_2
R = R_1 + R_2 + R_3
q = (t_w1 - t_f2) / R
print(f'单位面积传递的热量为{q:.2f} W/m^2')
