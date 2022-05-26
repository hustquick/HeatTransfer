delta_1, delta_2, delta_3 = 0.794e-3, 152e-3, 9.5e-3
lambda_1, lambda_2, lambda_3 = 45, 0.07, 0.1
area = 37.2
t_in = -2
t_out = 30
h_in = 1.5
h_out = 2.5

tau = 1*3600

R_1 = delta_1 / (lambda_1 * area)
R_2 = delta_2 / (lambda_2 * area)
R_3 = delta_3 / (lambda_3 * area)
R_in = 1 / (h_in * area)
R_out = 1 / (h_out * area)
R_total = R_1 + R_2 + R_3 + R_in + R_out

q = (t_out - t_in) / R_total
Q = q * tau
print(f'Phi = {Phi:.2f} J')
