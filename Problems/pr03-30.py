import numpy as np
from scipy.optimize import root
from Functions.UnsteadyStateConduction import theta_to_theta_0_ratio, get_a, get_mu, get_Bi, get_Fo
import matplotlib.pyplot as plt
from scipy.integrate import solve_bvp

T_oo = 2300
T_m = 1500
delta = 10e-3
lambda_ = 10
a = 6e-6
h = 2500
T_0 = 300

# 保守估计时，认为陶瓷和喷管之间绝热
# 此时可将陶瓷层看做无限大平板处理
l_c = delta
shape = 'P'

Bi = get_Bi(l_c, lambda_, h)
mu = get_mu(Bi, shape)


def expressions(p):
    tau = p
    Fo = get_Fo(tau, l_c, a)
    xpr = T_m - T_oo - (T_0 - T_oo) * theta_to_theta_0_ratio(mu, 0, Fo, shape)
    return xpr


guess_value = 1
tau = root(expressions, guess_value).x[0]
print(f'tau = {tau:.0f} s')

Fo = get_Fo(tau, l_c, a)
if np.any([Fo]) <= 0.2:
    print('Fo数不满足上述公式的要求，上述结果不可靠！')
