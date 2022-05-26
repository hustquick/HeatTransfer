from functions import spherical_wall_R
from scipy.constants import day

d = 300e-3
delta = 30e-3
lambda_ = 1.8e-4
t = -195.6
t_a = 25
gamma = 199.6e3
time = 1*day

R = spherical_wall_R(d/2, d/2+delta, lambda_)
Phi = (t_a - t) / R
m = Phi * time / gamma
print(f'上述条件下，液氮每天的蒸发量为：{m:.2f} kg')
