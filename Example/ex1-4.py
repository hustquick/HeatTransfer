import numpy as np

h_1 = 8700
h_2 = 1800
delta = 1.5e-3
lambda_ = 383

R_1 = 1 / h_1
R_2 = 1 / h_2
R_3 = delta / lambda_
ratio = np.array([R_1, R_2, R_3])
ratio = ratio / ratio.sum()
