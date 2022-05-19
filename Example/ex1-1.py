import numpy as np

delta = 50e-3
t_w1 = 300
t_w2 = 100

lambda_ = np.array([375, 36.4, 2.32, 0.242])
q = lambda_ * (t_w1 - t_w2) / delta

print(f"(1)q = {q[0]:.2e}; (2)q = {q[1]:.2e}; (3)q = {q[2]:.2e}; (4)q = {q[3]:.2e}")
