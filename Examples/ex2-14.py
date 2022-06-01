delta = 50e-3
l_1, l_2, l_3 = 50e-2, 50e-2, 55e-2 + delta
lambda_ = 0.029
t_in = -5
t_out = 25

# 根据表格2-2
S_corner = 8 * 0.15 * delta
length_1 = l_1 - 2*delta
length_2 = l_2 - 2*delta
length_3 = l_3 - 2*delta
length_total = 4 * (length_1 + length_2 + length_3)
S_edge = 0.54 * length_total
A_wall_1 = (l_1 - 2 * delta) * (l_2 - 2 * delta)
A_wall_2 = (l_2 - 2 * delta) * (l_3 - 2 * delta)
A_wall_3 = (l_3 - 2 * delta) * (l_1 - 2 * delta)
A_total = 2 * (A_wall_1 + A_wall_2 + A_wall_3)
S_wall = A_total / delta
S_total = S_corner + S_edge + S_wall
Phi = lambda_ * S_total * (t_out - t_in)
print(f'Phi = {Phi:.2f} W')
