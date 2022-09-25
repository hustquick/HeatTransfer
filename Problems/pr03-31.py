import numpy as np
from scipy.optimize import root
from Functions.UnsteadyStateConduction import theta_to_theta_0_ratio, get_a, get_mu, get_Bi, get_Fo
import matplotlib.pyplot as plt
from scipy.integrate import solve_bvp
from Functions.Self_defined import check_Fo

delta = 9e-3
t_0 = 30
h = 1950
rho = 8400
c = 560
lambda_ = 24.6
t_oo = 1750
t_w = 1000

l_c = delta
shape = 'P'

Bi = get_Bi(l_c, lambda_, h)
mu = get_mu(Bi, shape)
a = get_a(lambda_, rho, c)


def expressions(p):
    tau = p
    Fo = get_Fo(tau, l_c, a)
    xpr = t_w - t_oo - (t_0 - t_oo) * theta_to_theta_0_ratio(mu, 1, Fo, shape)
    return xpr


guess_value = [1]
tau = root(expressions, guess_value).x[0]
print(f'(1) tau = {tau:.0f} s')

Fo = get_Fo(tau, l_c, a)
t_m = t_oo + (t_0 - t_oo) * theta_to_theta_0_ratio(mu, 0, Fo, shape)
Delta_t = t_w - t_m
print(f'(2) Delta_t = {Delta_t:.2f}degC')

average = Delta_t / delta
# 由于在壁面处热流密度最大，所以壁面处温度梯度最大
# q = lambda_ * partial_t / partial_x = h * (t_oo - t_0)
max_gradient = h * (t_oo - t_w) / lambda_
print(f'(3) 平均温度梯度为 {average:.2f}degC/m, 最大温度梯度为 {max_gradient:.2f}degC/m')

check_Fo(Fo)
