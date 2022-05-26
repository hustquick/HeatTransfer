import numpy as np

a = np.arange(-50, 100, 10)
b = np.arange(100, 200, 20)
c = np.arange(200, 400, 50)
d = np.arange(400, 1300, 100)
temperature_list = np.concatenate((a, b, c, d))

density_list = np.array([
    1.584, 1.515, 1.453, 1.395, 1.342, 1.293, 1.247,
    1.205, 1.165, 1.128, 1.093, 1.060, 1.029, 1.000,
    0.972, 0.946, 0.898, 0.854, 0.815, 0.779, 0.746,
    0.674, 0.615, 0.566, 0.524, 0.456, 0.404, 0.362,
    0.329, 0.301, 0.277, 0.257, 0.239,
])

lambda_list = np.array([
    2.04, 2.12, 2.20, 2.28, 2.36, 2.44, 2.51,
    2.59, 2.67, 2.76, 2.83, 2.90, 2.96, 3.05,
    3.13, 3.21, 3.34, 3.49, 3.64, 3.78, 3.93,
    4.27, 4.60, 4.91, 5.21, 5.74, 6.22, 6.71,
    7.18, 7.63, 8.07, 8.50, 9.15,
    ]) * 1e-2
