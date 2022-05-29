import numpy as np

t_1 = 80
t_2 = 25
lambda_ = 1.5
length = 1

l = 1
d = 0.5

S = 2 * np.pi * length / (np.log(1.08 * l / d))
Phi = S * lambda_ * (t_1 - t_2)
print(f'每米长烟道上的散热量为：{Phi:.2f} W')
