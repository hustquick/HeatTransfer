a = b = 10e-3
t_a = 20
t_max = 85
h = 175
delta = 1e-3

A = a * b + 2 * delta * a + 2 * delta * b
Q = h * A * (t_max - t_a)
print(f'不考虑辐射时，芯片的最大允许功率为：{Q:.2f} W')
