import scipy.constants as sc

import sys
sys.path.append("..")
from Functions.SteadyStateConduction import spherical_wall_R, cylindrical_wall_R


delta = 20e-2
lambda_ = 1.5

T_i = 400
t_f = 25
h = 10
r_o = 0.5
l = 2.0

t_i = sc.convert_temperature(T_i, 'K', 'C')

# 可将导热热阻开成球壳热阻和圆柱壳热阻的并联
# 圆柱壳热阻
R_c = cylindrical_wall_R(r_o - delta, r_o, lambda_, l)
# 球壳热阻
R_s = spherical_wall_R(r_o - delta, r_o, lambda_)

R = 1 / (1 / R_c + 1 / R_s)
Phi = (t_i - t_f) / R
print(f'所需的电加热器的功率为：{Phi:.2f} W')
