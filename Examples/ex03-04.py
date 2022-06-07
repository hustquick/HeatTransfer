from Functions.UnsteadyStateConduction import get_Bi, theta_to_theta_m_ratio, theta_to_theta_0_ratio
import numpy as np
from scipy.optimize import root

delta = 100e-3
t_oo = 1000
t_0 = 20
t = 500

h = 174
lambda_ = 34.8
a = 0.555e-5
Bi_list = [0.1, 0.5, 1.0]
mu_list = [0.3111, 0.6533, 0.8603]
shape = 'P'

Bi = get_Bi(delta, lambda_, h)
mu = np.interp(Bi, Bi_list, mu_list)

x = delta
eta = x/delta

theta = t - t_oo
t_m = t_oo + theta / theta_to_theta_m_ratio(mu, eta, shape)
delta_T_m = abs(t - t_m)
print(f'剖面上的最大温差为：{delta_T_m:.2f} C')


def expressions(p):
    Fo = p
    xpr = (t - t_oo) / (t_0 - t_oo) - theta_to_theta_0_ratio(mu, eta, Fo, shape)
    return xpr


guess_values = [1]
Fo = root(expressions, guess_values).x[0]
l_c = delta
tau = Fo * l_c**2 / a
print(f'所需的时间为：{tau:.0f} s')

if np.any([Fo]) <= 0.2:
    print('Fo数不满足上述公式的要求，上述结果不可靠！')
