import numpy as np
from scipy.integrate import quad

a_list = np.array([0.506, 0.08, 20.24])
n_list = np.array([0.5, 0.0, 1.5])
x_1 = 25e-3
x_2 = 125e-3

number = len(a_list)
result = np.zeros(number)
for i in range(number):
    a = a_list[i]
    n = n_list[i]

    def func(x):
        d = a*x**n
        area = np.pi / 4 * d**2
        return 1/area
    result[i] = 1 / quad(func, x_1, x_2)[0]

arg = np.argsort(-result)
for i in range(number):
    print(f'第{arg[i]+1}种导热问题热流量排第{i+1}')
