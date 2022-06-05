from Functions.UnsteadyStateConduction import get_mu, theta_to_theta_0_ratio
from scipy.optimize import root
import numpy as np

d = 400e-3
t_0 = 20
t_oo = 900
t = 750

h = 174
lambda_ = 34.8
a = 0.695e-5
shape = 'C'

l_c = d / 2
eta = 1
Bi = h * l_c / lambda_
mu = get_mu(Bi, shape)

ratio_w_to_0 = (t - t_oo)/(t_0 - t_oo)


def expressions(p):
    Fo = p
    return ratio_w_to_0 - theta_to_theta_0_ratio(mu, eta, Fo, shape)


guess_values = np.ones(1)
Fo = root(expressions, guess_values).x[0]
tau = Fo * l_c**2 / a
print(f'所需的时间为：{tau:.0f} s')
