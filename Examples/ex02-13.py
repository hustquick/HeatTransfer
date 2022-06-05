import numpy as np
from Functions.SteadyStateConduction import cylindrical_wall_R, fin_tip_R, fin_tip_efficiency

d_1 = 4e-3
thickness = 6e-3   # 环的的厚度
length = 0.01   # 肋片高度，课本缺失
delta_al = 1e-3
lambda_al = 200
delta = 0.7e-3
R_A_ct = 1e-3
t_air = 20
h_air = 25
t = 80
N = 12

A_ct = np.pi * d_1 * thickness
R_ct = R_A_ct / A_ct    # 接触热阻
# 铝圈导热热阻
R_al = cylindrical_wall_R(d_1 / 2, d_1 / 2 + delta_al, lambda_al, thickness)
A_c = thickness * delta
perimeter = 2 * (thickness + delta)
# 每根肋片热阻
R_f = fin_tip_R(length+delta/2, perimeter, A_c, lambda_al, h_air)

# 肋片的总热阻
R_f_12 = R_f / 12
# 根部热阻
R_r = 1 / (h_air * (np.pi * (d_1 + 2 * delta_al) - N * delta) * thickness)
# 肋片的总等效热阻
R_eq = 1 / (1/ R_f_12 + 1/ R_r)

# 总热阻
R_total = R_ct + R_al + R_eq

Phi = (t - t_air) / R_total

print(f'晶体管的散热量为：{Phi:.2f} W')

eta_f = fin_tip_efficiency(length, perimeter, A_c, lambda_al, h_air)
