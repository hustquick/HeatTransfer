import numpy as np
from scipy.optimize import root
from Functions.UnsteadyStateConduction import theta_to_theta_0_ratio, a, mu, Bi, Fo
import matplotlib.pyplot as plt

d = 20e-3
shape = 'S'
t_0 = 650
t_oo = 20
t_m = 450
dt_dtau_list = np.array([180, 360])
rho = 10500
c = 262
lambda_ = 360

a = a(lambda_, rho, c)
tau_list = abs(t_m - t_0) / dt_dtau_list
l_c = d/2   # 后续用到的公式都是基于半径r为特征长度的公式
eta = 0

for i, tau in enumerate(tau_list):
    def expressions(p):
        h = p[0]
        Bi_v = Bi(l_c, lambda_, h)
        mu_v = mu(Bi_v, shape)
        Fo_v = Fo(tau, l_c, a)
        xpr = (t_m - t_oo)/(t_0 - t_oo) - theta_to_theta_0_ratio(mu_v, eta, Fo_v, shape)
        return xpr


    guess_values = 3000
    h = root(expressions, guess_values).x[0]
    print(f'({i+1}) h = {h:.0f} W/m^2-K')

