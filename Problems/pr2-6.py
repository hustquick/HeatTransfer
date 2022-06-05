d_o = 130e-3
delta = 2.1e-3
lambda_ = 23.2
t_o = 240
q = 4.8e6
t_i_max = 700

delta_t = q * delta / lambda_
t_i = t_o + delta_t
if t_i < t_i_max:
    print('该燃烧室工作于安全温度范围内')
else:
    print('该燃烧室工作于安全温度范围外')
