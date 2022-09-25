import scipy.constants as sc
from scipy.optimize import root

Q = 1200    # 电熨斗的功率，课本缺失
A = 300e-4
epsilon = 0.9
t_a = 25
h = 39

T_a = sc.convert_temperature(t_a, 'C', 'K')


def expressions(p):
    Q_rad, Q_conv, T = p
    exp1 = Q_rad - epsilon * sc.sigma * A * (T**4 - T_a**4)
    exp2 = Q_conv - h * A * (T - T_a)
    exp3 = Q_rad + Q_conv - Q
    return [exp1, exp2, exp3]


guess_value = [Q/2, Q/2, T_a + 10]
Q_rad, Q_conv, T = root(expressions, guess_value).x
t = sc.convert_temperature(T, 'K', 'C')
print(f'T = {T:.2f} K')
print(f't = {t:.2f}degC')
