from Functions.SteadyStateConduction import plate_wall_Delta_T_with_heat_source

# 绝热表面可以看做对称面
delta = 7e-2
t_f = 30
q_dot = 0.3e6
h = 450
lambda_ = 18

Delta_T = plate_wall_Delta_T_with_heat_source(2*delta, lambda_, h, q_dot)
t_max = t_f + Delta_T
print(f't_max = {t_max:.2f} C')
