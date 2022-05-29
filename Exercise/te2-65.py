delta = 300e-3
lambda_ = 0.8
t_i= 400
t_o= 50

S = 0.15 * delta
Phi = lambda_ * S * (t_i - t_o)
print(f'热损失为：{Phi:.2f} W')
