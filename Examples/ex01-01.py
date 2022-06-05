import numpy as np

delta = 50e-3
t_w1 = 300
t_w2 = 100

lambda_ = np.array([375, 36.4, 2.32, 0.242])
q = lambda_ * (t_w1 - t_w2) / delta

for i, q_ in enumerate(q):
    print(f"({i+1}) q = {q_:.2e} W/m^2")
