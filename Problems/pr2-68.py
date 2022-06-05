from scipy.optimize import root
import numpy as np

l_1, l_2, l_3 = 0.5, 0.75, 0.75
lambda_ = 0.02
t_i = -10
t_o = 30
Phi = 45


def expressions(p):
    delta = p
    S_corner = 4 * 0.15 * delta

    length_1 = l_1 - 2*delta
    length_2 = l_2 - 2*delta
    length_3 = l_3 - 2*delta
    length_total = 4 * length_1 + 2 * (length_2 + length_3)
    S_edge = 0.54 * length_total

    A_wall_1 = (l_1 - 2 * delta) * (l_2 - 2 * delta)
    A_wall_2 = (l_2 - 2 * delta) * (l_3 - 2 * delta)
    A_wall_3 = (l_3 - 2 * delta) * (l_1 - 2 * delta)
    A_total = 2 * (A_wall_1 + A_wall_3) + A_wall_2
    S_wall = A_total / delta

    S_total = S_corner + S_edge + S_wall
    xpr = Phi - lambda_ * S_total * (t_o - t_i)
    return xpr


guess_value = np.array([l_1 / 10])
delta = root(expressions, guess_value).x[0]
print(f'delta = {delta:.3f} m')
