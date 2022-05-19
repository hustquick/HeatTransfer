A = 12
delta = 260e-3
lambda_ = 1.5
t_i = 25
t_o = -5

Q = A * lambda_ * (t_i - t_o) / delta
print(f'此砖墙向外界散失的热量为{Q:.2f} J')
