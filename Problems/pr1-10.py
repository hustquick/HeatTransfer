import scipy.constants as sc

delta = 13e-2
A = 20
lambda_ = 1.04
t_i = 520
t_o = 50
q = 2.09e4*1e3
tau = 1 * sc.day
Q = A * lambda_ * (t_i - t_o) / delta
m = Q * tau / q
print(f'每天因热损失要用掉{m:.2f} kg煤')
