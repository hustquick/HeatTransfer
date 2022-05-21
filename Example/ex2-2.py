from Appendix4_lambda_ import lambda_
from scipy.optimize import root

material1 = '耐火黏土砖'
material2 = 'B 级硅藻土制品'
material3 = '石棉板'

delta1 = 115e-3
delta2 = 125e-3
delta3 = 70e-3

t_in = 495
t_out = 60

tau = 3600

lambda_3 = 0.116    # 根据附录4无法查知石棉板的导热系数，这里只能取课本给的值


def expressions(p):
    t_12, t_23, q = p
    expr1 = q - lambda_(material1, (t_in + t_12)/2) * (t_in - t_12) / delta1
    expr2 = q - lambda_(material2, (t_12 + t_23)/2) * (t_12 - t_23) / delta2
    expr3 = q - lambda_3 * (t_23 - t_out) / delta3
    return expr1, expr2, expr3


guess_value = [t_in - 10, t_in - 20, 1]
t_12, t_23, q = root(expressions, guess_value).x
Q = q * tau
print(f'Q = {Q:.2f} J/m^2-h')
print(f't_12 = {t_12:.2f}C')

