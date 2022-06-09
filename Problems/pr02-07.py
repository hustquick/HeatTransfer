import numpy as np

P_total = 1000
eta = 85/100
delta = 3e-3
d = 200e-3
lambda_ = 18
h = 2500
t_f = 95

P = P_total * eta
area = np.pi * d**2 / 4
R_1 = 1 / (h * area)
R_2 = delta / lambda_
R = R_1 + R_2
t_bot = t_f + P * R
t_top = t_f + P * R_1
print(f't_bot = {t_bot:.2f} C')
print(f't_top = {t_top:.2f} C')
