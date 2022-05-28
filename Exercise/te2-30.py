from sympy import symbols, diff, Function, pi, dsolve, solve, integrate

height = 30e-2
d_1 = 8.2e-2
d_2 = 13e-2
t_1 = 20
t_2 = 520
lambda_ = 100

A = Function('A')
t = symbols('t')
Phi = symbols('Phi')
y = symbols('y')

eq1 = diff(A(y), y, 2)
A = solve(dsolve(eq1, ics={A(0): pi/4*d_2**2, A(height): pi/4*d_1**2}), A(y))[0]
# Phi = -lambda_*A*diff(t, y)
result1 = integrate(-1/(lambda_ * A), (y, 0, height))
result2 = integrate(1, (t, t_2, t_1))
Phi = result2 / result1
print(f'Phi = {Phi:.2f} W')
