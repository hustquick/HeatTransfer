from Functions.UnsteadyStateConduction import mu, theta_to_theta_0_ratio
from scipy.optimize import root

d = 400e-3
t_0 = 20
t_oo = 900
t = 750

h = 174
lambda_ = 34.8
a = 0.695e-5
shape = 'C'

r = d/2
eta = 1
Bi = h*r/lambda_
mu = mu(Bi, shape)

ratio_w_to_0 = (t - t_oo)/(t_0 - t_oo)


def expressions(p):
    Fo = p
    return ratio_w_to_0 - theta_to_theta_0_ratio(mu, eta, Fo, shape)


guess_values = 1
Fo = root(expressions, guess_values).x[0]
l_c = r
tau = Fo * l_c**2 / a
print(f'所需的时间为：{tau:.0f} s')
