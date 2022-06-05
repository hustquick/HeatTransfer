from sympy import symbols, pi, diff, Function, dsolve, solve

d, l, t_1, t_2, t_f, lambda_, h = symbols('d, l, t_1, t_2, t_f, lambda_, h')
x = symbols('x')
t = Function('t')

eq1 = diff(t(x), x, 2)
result = dsolve(eq1, ics={t(0): t_1, t(l): t_2})
t = solve(result, t(x))[0]
print(f'(1) t(x) = {t}')

t = Function('t')
eq2 = diff(t(x), x, 2) - 4 * h / (d * lambda_) * (t(x) - t_f)
result = dsolve(eq2, ics={t(0): t_1, t(l): t_2})
t = solve(result, t(x))[0]
print(f'(2) t(x) = {t}')
