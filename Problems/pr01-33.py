import numpy as np

delta = 200e-3
h = 3
w = 6
t_in = 2
t_out = -10
h_in = 6
ratio_list = [1, 0.5, 0.25]
h_out_base = 60
h_out = h_out_base * np.array(ratio_list)
lambda_ = 0.044

R_1 = 1 / h_in
R_2 = delta / lambda_
R_3 = 1 / h_out
R = R_1 + R_2 + R_3
A = h * w
Q = A * (t_in - t_out) / R
for i, ratio in enumerate(ratio_list):
    print(f'当风速减小为原来的{ratio:.0%}时，散热量为{Q[i]:.2f} W')
