h_1 = 95
delta = 2.5e-3
lambda_ = 46.5
h_2 = 5800

delta2 = 2e-3
lambda_2 = 0.116
delta3 = 1e-3
lambda_3 = 1.15

R_1 = 1 / h_1
R_2 = 1 / h_2
R_3 = delta / lambda_
R_4 = delta2 / lambda_2
R_5 = delta3 / lambda_3

R = R_1 + R_2 + R_3 + R_4 + R_5
h = 1 / R
print(f'h = {h:.2f} W/(m^2-W)')
