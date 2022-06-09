from Functions.UnsteadyStateConduction import t_x_for_constant_q_0, get_mu, theta_to_theta_0_ratio, Q_to_Q_0_ratio
import scipy.constants as sc
from CoolProp.CoolProp import PropsSI as psi
import numpy as np
from scipy.optimize import root
from Functions.Self_defined import check_Fo

d = 10e-2
height = 8e-2
t_0 = 40
t_oo = 105
tau = 80*60
shape = ['P', 'C']

# 物性参数可以选择水在温度为初始温度和最终温度的平均值时的物理参数
# 相变换热系数h很大，可认为h = np.inf
material = 'Water'
h = np.inf

# 先求出蔬菜罐头的质量
T_0 = sc.convert_temperature(t_0, 'C', 'K')
rho_0 = psi('D', 'T', T_0, 'P', sc.atm, material)
V = np.pi * d**2 / 4 * height
m = rho_0 * V


def expressions(p):
    t = p
    t_a = (t_0 + t)/2
    T_a = sc.convert_temperature(t_a, 'C', 'K')
    rho = psi('D', 'T', T_a, 'P', sc.atm, material)
    c = psi('C', 'T', T_a, 'P', sc.atm, material)
    lambda_ = psi('L', 'T', T_a, 'P', sc.atm, material)
    a = lambda_ / (rho * c)

    # 先考虑厚度方向，作为无限大平板进行分析
    l_c_1 = height / 2
    Bi_1 = h * l_c_1 / lambda_
    Fo_1 = a * tau / l_c_1**2
    mu_1 = get_mu(Bi_1, shape[0])
    eta_1 = 0
    ratio_m_to_0_1 = theta_to_theta_0_ratio(mu_1, eta_1, Fo_1, shape[0])
    Q_to_Q_0_1 = Q_to_Q_0_ratio(mu_1, Fo_1, shape[0])

    # 再考虑径向，作为无限长圆柱进行分析
    l_c_2 = d / 2
    Bi_2 = h * l_c_2 / lambda_
    Fo_2 = a * tau / l_c_2**2
    mu_2 = get_mu(Bi_2, shape[1])
    eta_2 = 0
    ratio_m_to_0_2 = theta_to_theta_0_ratio(mu_2, eta_2, Fo_2, shape[1])
    Q_to_Q_0_2 = Q_to_Q_0_ratio(mu_2, Fo_2, shape[1])

    ratio_m_to_0 = ratio_m_to_0_1 * ratio_m_to_0_2
    t_m = t_oo + ratio_m_to_0 * (t_0 - t_oo)
    xpr = t - t_m
    return xpr


guess_value = t_0 + 10
t = root(expressions, guess_value).x[0]
t_m = t
print(f't_m = {t_m:.2f} C')

t_a = (t_0 + t)/2
T_a = sc.convert_temperature(t_a, 'C', 'K')
rho = psi('D', 'T', T_a, 'P', sc.atm, material)
c = psi('C', 'T', T_a, 'P', sc.atm, material)
lambda_ = psi('L', 'T', T_a, 'P', sc.atm, material)
a = lambda_ / (rho * c)

# 先考虑厚度方向，作为无限大平板进行分析
l_c_1 = height / 2
Bi_1 = h * l_c_1 / lambda_
Fo_1 = a * tau / l_c_1 ** 2
mu_1 = get_mu(Bi_1, shape[0])
eta_1 = 0
ratio_m_to_0_1 = theta_to_theta_0_ratio(mu_1, eta_1, Fo_1, shape[0])
Q_to_Q_0_1 = Q_to_Q_0_ratio(mu_1, Fo_1, shape[0])

# 再考虑径向，作为无限长圆柱进行分析
l_c_2 = d / 2
Bi_2 = h * l_c_2 / lambda_
Fo_2 = a * tau / l_c_2 ** 2
mu_2 = get_mu(Bi_2, shape[1])
eta_2 = 0
ratio_m_to_0_2 = theta_to_theta_0_ratio(mu_2, eta_2, Fo_2, shape[1])
Q_to_Q_0_2 = Q_to_Q_0_ratio(mu_2, Fo_2, shape[1])

Q_to_Q_0 = Q_to_Q_0_1 + Q_to_Q_0_2 - Q_to_Q_0_1 * Q_to_Q_0_2
t_b = (t_0 + t_m)/2
T_b = sc.convert_temperature(t_b, 'C', 'K')
c_b = psi('C', 'T', T_b, 'P', sc.atm, material)
Q_0 = c_b * m * (t_oo - t_0)
Q = Q_0 * Q_to_Q_0
print(f'Q = {Q:.0f} J')

Fo = [Fo_1, Fo_2]
check_Fo(Fo)
