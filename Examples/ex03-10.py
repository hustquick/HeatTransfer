from Functions.UnsteadyStateConduction import get_mu, \
    theta_to_theta_0_ratio, Q_to_Q_0_ratio
from scipy.optimize import root
import numpy as np
from CoolProp.CoolProp import PropsSI as psi
import scipy.constants as sc
from Functions.Self_defined import check_Fo

D = 4e-2
H = 6e-2
shape = ['P', 'C']
t_0 = 10
t_oo = 180
h = 15
t_m = 80
material = 'water'  # 用水的物性参数替代牛肉的物性参数
# 以（10°C+80°C)/2=45°C来确定从开始加热到中心温度为 80c水的物理特性，
# 以（10°C+180°C)/2=95°C来确定计算总加热量的物性。

# 先求出牛肉块的质量
T_0 = sc.convert_temperature(t_0, 'C', 'K')
rho_0 = psi('D', 'T', T_0, 'P', sc.atm, material)
V = np.pi * D**2 * H / 4
m = rho_0 * V

t_a = (t_0 + t_m) / 2
t_b = (t_0 + t_oo) / 2

T_a = sc.convert_temperature(t_a, 'C', 'K')
rho_a = psi('D', 'T', T_a, 'P', sc.atm, material)
c_a = psi('C', 'T', T_a, 'P', sc.atm, material)
lambda_a = psi('L', 'T', T_a, 'P', sc.atm, material)
a_a = lambda_a / (c_a * rho_a)


def expressions(p):
    tau = p
    # 先考虑厚度方向，作为无限大平板进行分析
    l_c_1 = H / 2
    Bi_1 = h * l_c_1 / lambda_a
    Fo_1 = a_a * tau / l_c_1**2
    mu_1 = get_mu(Bi_1, shape[0])
    eta_1 = 0
    ratio_m_to_0_1 = theta_to_theta_0_ratio(mu_1, eta_1, Fo_1, shape[0])

    # 再考虑径向，作为无限长圆柱进行分析
    l_c_2 = D / 2
    Bi_2 = h * l_c_2 / lambda_a
    Fo_2 = a_a * tau / l_c_2**2
    mu_2 = get_mu(Bi_2, shape[1])
    eta_2 = 0
    ratio_m_to_0_2 = theta_to_theta_0_ratio(mu_2, eta_2, Fo_2, shape[1])

    ratio_m_to_0 = ratio_m_to_0_1 * ratio_m_to_0_2
    xpr = t_m - t_oo - ratio_m_to_0 * (t_0 - t_oo)
    return xpr


guess_values = np.ones(1)
tau = root(expressions, guess_values).x[0]
print(f'tau = {tau:.0f} s')

# 先考虑厚度方向，作为无限大平板进行分析
l_c_1 = H / 2
Bi_1 = h * l_c_1 / lambda_a
Fo_1 = a_a * tau / l_c_1**2
mu_1 = get_mu(Bi_1, shape[0])
Q_to_Q_0_1 = Q_to_Q_0_ratio(mu_1, Fo_1, shape[0])

# 再考虑径向，作为无限长圆柱进行分析
l_c_2 = D / 2
Bi_2 = h * l_c_2 / lambda_a
Fo_2 = a_a * tau / l_c_2**2
mu_2 = get_mu(Bi_2, shape[1])
Q_to_Q_0_2 = Q_to_Q_0_ratio(mu_2, Fo_2, shape[1])

Q_to_Q_0 = Q_to_Q_0_1 + Q_to_Q_0_2 * (1 - Q_to_Q_0_1)

T_b = sc.convert_temperature(t_b, 'C', 'K')
rho_b = psi('D', 'T', T_b, 'P', sc.atm, material)
c_b = psi('C', 'T', T_b, 'P', sc.atm, material)
Q_0 = c_b * m * (t_oo - t_0)
Q = Q_0 * Q_to_Q_0
print(f'Q = {Q:.0f} J')

Fo = [Fo_1, Fo_2]
check_Fo(Fo)
