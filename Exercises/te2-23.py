from Functions.SteadyStateConduction import spherical_wall_R

d = 2
delta = 1e-2
t = -40
delta_insu = 30e-2
lambda_ = 0.08
t_a = 40
h_insu = 30
number = 10

r_1 = d/2 + delta   # 认为绝缘层内壁温度等于罐内温度，只分析绝缘层的传热
r_2 = d/2 + delta + delta_insu
R = spherical_wall_R(r_1, r_2, lambda_)
Phi = number * (t_a - t) / R
print(f'10 个球罐所必须配备的制冷设备的容量为：{Phi:.2f} W')
