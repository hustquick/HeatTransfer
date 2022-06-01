delta_1 = 14e-3
delta_2 = 6e-3
Phi_dot = 1.5e7
lamdba_1 = 35
lambda_2 = 100
t_f = 150
h = 3500

q = delta_1/2 * Phi_dot
t_2 = t_f + q / h
t_1 = q * delta_2 / lambda_2 + t_2
t_0 = t_1 + Phi_dot * (delta_1 / 2)**2 / (2*lamdba_1)
print(f't_0 = {t_0:.2f}')
