a = 60e-2
b = 30e-2
delta = 4e-3
t_in = 20
t_out = -20
h_in = 10
h_out = 50
lambda_ = 0.78

R_1 = 1 / h_in
R_2 = delta / lambda_
R_3 = 1 / h_out
R = R_1 + R_2 + R_3
A = a * b
Q = (t_in - t_out) / R * A
print(f'通过玻璃的热损失为：{Q:.2f} W')
