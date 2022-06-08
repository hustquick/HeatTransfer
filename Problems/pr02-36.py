import numpy as np
from scipy.optimize import root

q = 1000
delta = 20e-3
x_list = np.array([0, 10e-3, 20e-3])
t_list = np.array([100, 60, 40])


# lambda_ = lambda_0 * (1 + b*t)


def lambda_(delta, delta_t):
    return -q * delta / delta_t


def expressions(p):
    lambda_0, b = p

    def lambda_b(t):
        return lambda_0 * (1 + b * t)

    delta_1 = x_list[1] - x_list[0]
    delta_2 = x_list[2] - x_list[1]
    delta_t_1 = t_list[1] - t_list[0]
    delta_t_2 = t_list[2] - t_list[1]
    t_average_1 = (t_list[1] + t_list[0]) / 2
    t_average_2 = (t_list[2] + t_list[1]) / 2
    xpr1 = lambda_(delta_1, delta_t_1) - lambda_b(t_average_1)
    xpr2 = lambda_(delta_2, delta_t_2) - lambda_b(t_average_2)
    return xpr1, xpr2


guess_values = [1, 1]
lambda_0, b = root(expressions, guess_values).x
print(f'lambda_0 = {lambda_0:.3f} W/m-K')
print(f'b = {b:.3e} K^-1')
