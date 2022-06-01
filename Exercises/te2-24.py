from scipy.optimize import root
from Functions.SteadyStateConduction import spherical_wall_R

d_i = 0.15
d_o = 0.25
t_i = 200
t_o = 40
P = 56.5

R = P / (t_i - t_o)
guess_value = 1
lambda_ = root(lambda lambda_: R - spherical_wall_R(d_i/2, d_o/2, lambda_), guess_value).x[0]
print(f'lambda = {lambda_:.2f} W/m-K')
