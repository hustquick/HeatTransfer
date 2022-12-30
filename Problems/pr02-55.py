import sys
sys.path.append("..")
from Functions.SteadyStateConduction import fin_tip_Delta_T_ratio, fin_tip_efficiency

H = 9e-2
perimeter = 7.6e-2
A_c = 1.95e-4
t_0 = 305
t_f = 815
h = 28
lambda_ = 55

y = H/2

Delta_T_ratio_y = fin_tip_Delta_T_ratio(y, perimeter, A_c, lambda_, h)
t_y = t_f - Delta_T_ratio_y*(t_f - t_0)
print(f'该柱体中间截面上的平均温度为{t_y:.2f}degC')

Delta_T_ratio_H = fin_tip_Delta_T_ratio(H, perimeter, A_c, lambda_, h)
t_H = t_f - Delta_T_ratio_H*(t_f - t_0)
print(f'该柱体的最高温度温度为{t_H:.2f}degC')

efficiency = fin_tip_efficiency(H, perimeter, A_c, lambda_, h)
Phi = efficiency * h * perimeter * H * (t_f - t_0)
print(f'冷却介质带走的热量为为{Phi:.2f} W')
