import numpy as np
from scipy.optimize import root
import sys
sys.path.append("..")
from Functions.UnsteadyStateConduction import theta_to_theta_0_ratio, get_a, get_mu, get_Bi, get_Fo
from Functions.Self_defined import check_Fo

d = 20e-3
shape = 'S'
t_0 = 650
t_oo = 20
t_m = 450
dt_dtau_list = np.array([180, 360])
rho = 10500
c = 262
lambda_ = 360

a = get_a(lambda_, rho, c)
tau_list = abs(t_m - t_0) / dt_dtau_list
l_c = d/2   # 后续用到的公式都是基于半径r为特征长度的公式
eta = 0

for i, tau in enumerate(tau_list):
    def expressions(p):
        h = p[0]
        Bi = get_Bi(l_c, lambda_, h)
        mu = get_mu(Bi, shape)
        Fo = get_Fo(tau, l_c, a)
        xpr = (t_m - t_oo)/(t_0 - t_oo) - theta_to_theta_0_ratio(mu, eta, Fo, shape)
        return xpr


    guess_values = 3000
    h = root(expressions, guess_values).x[0]
    print(f'({i+1}) h = {h:.0f} W/m^2-K')

    Fo = get_Fo(tau, l_c, a)
    check_Fo(Fo)

