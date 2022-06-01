from sympy.abc import t
from sympy import solve, symbols

delta = 25e-3
t_1 = 40
t_2 = 85
phi = 1.82e3
area = 0.2

lmbda_ = phi * delta / (area * (t_2 - t_1))
print(f'lmbda = {lmbda_:.2f}')

# 如果已知平板中间的温度t，则可以得到lmbda的公式

lambda_1 = phi * delta / (area * (t - t_1))
lambda_2 = phi * delta / (area * (t_2 - t))

lambda_0, b = symbols('lambda_0 b')

result = solve([lambda_1 - lambda_0 * (1 + b*(t+t_1)/2), lambda_2 - lambda_0 * (1 + b*(t+t_2)/2)], lambda_0, b)
print(f'lambda_0 = {result[0][0]}')
print(f'b = {result[0][1]}')

