from Functions.SteadyStateConduction import fin_tip_Delta_T_ratio
import numpy as np

d = 10e-3
delta = 1.0e-3
H = 120e-3
h = 25
t_0 = 25
t_f = 70
lambda_ = [390, 50]

perimeter = np.pi * d
A_c = np.pi * (d/2 + delta)**2 - np.pi * (d/2)**2
Delta_T = np.zeros(2)

for i, lambda_i in enumerate(lambda_):
    Delta_T_ratio = fin_tip_Delta_T_ratio(H, perimeter, A_c, lambda_i, h)
    Delta_T[i] = Delta_T_ratio * (t_f - t_0)
    print(f'({i+1}) Delta_T = {Delta_T[i]:.2f}degC')

delta_T12 = Delta_T[0] - Delta_T[1]
print(f'两温度计读数相差{abs(delta_T12):.2f}degC')

