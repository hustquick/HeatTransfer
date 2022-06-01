from sympy import symbols, diff, Function, dsolve, solve
import numpy as np

d, l, t_1, t_2, t_f, lambda_, h = symbols('d, l, t_1, t_2, t_f, lambda_, h')
x = symbols('x')

# eq1 = diff(t(x), x, 2)
# result = dsolve(eq1, ics={t(0): t_1, t(l): t_2})
# t = solve(result, t(x))[0]
# print(f'(1) t(x) = {t}')

t = Function('t')
eq2 = diff(t(x), x, 2) - 4 * h / (d * lambda_) * (t(x) - t_f)
result = dsolve(eq2, ics={t(0): t_1, t(l): t_2})
t = solve(result, t(x))[0]
print(f't(x) = {t}')

d = 20e-3
l = 300e-3
t_1 = 250
t_2 = 60
t_f = 30

h = 10
lambda_ = 40

area = np.pi * d ** 2 / 4
phi = - lambda_ * diff(t, x, 1) * area
phi_1 = phi.subs([(symbols('d'), d), (symbols('l'), l), (symbols('t_1'), t_1), (symbols('t_2'), t_2),
                  (symbols('t_f'), t_f), (symbols('h'), h), (symbols('lambda_'), lambda_), (symbols('x'), 0)])
phi_2 = phi.subs([(symbols('d'), 20e-3), (symbols('l'), l), (symbols('t_1'), t_1), (symbols('t_2'), t_2),
                  (symbols('t_f'), 30), (symbols('h'), h), (symbols('lambda_'), lambda_), (symbols('x'), l)])
phi_total = phi_1 + phi_2
print(f'钢柱体单位时间从两个热源分别获得的热量为:{phi_1:.2f} W 和{phi_2:.2f} W，总计{phi_total:.2f} W。')
