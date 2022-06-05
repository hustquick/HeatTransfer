from Functions.SteadyStateConduction import fin_tip_efficiency
import numpy as np

lambda_ = np.array([208, 41.5])
h = np.array([284, 511])
H = np.array([15.24e-3, 15.24e-3])
delta = np.array([2.54e-3, 2.54e-3])

perimeter = 2
A_c = delta
efficiency = fin_tip_efficiency(H, perimeter, A_c, lambda_, h)
# 也可以用fin_tip_efficiency2函数求解
# A_L = delta * H
# efficiency2 = fin_tip_efficiency2(H, A_L, lambda_, h)
np.set_printoptions(formatter={'float': '{:.2%}'.format})
print(efficiency)
