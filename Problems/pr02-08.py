from sympy import symbols, solve

t_h = 400
t_c = 300
Delta_t = 2.49
Delta_t1 = 3.56
Delta_t2 = 3.60

q, A, l, lambda_, lambda_1, lambda_2 = symbols('q A l lambda_ lambda_1 lambda_2')

xpr1 = q - Delta_t1 * A * lambda_1 / l
xpr2 = q - Delta_t2 * A * lambda_2 / l
xpr3 = q - Delta_t * A * lambda_ / l

result = solve([xpr1, xpr2, xpr3], [lambda_1, lambda_, lambda_2])
lambda_ = 2 * result[lambda_] / (result[lambda_1] + result[lambda_2]) * lambda_1
print(f'lambda_ = {lambda_}')

if Delta_t1 == Delta_t2:
    print('标准材料的导热系数随温度发生变化时，Delta_t1与Delta_t2相等')
else:
    print('标准材料的导热系数随温度发生变化时，Delta_t1与Delta_t2不等')
