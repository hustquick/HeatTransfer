import numpy as np
import scipy.constants

from Functions.UnsteadyStateConduction import theta_to_theta_0_ratio, Q_to_Q_0_ratio, get_mu, get_Bi, get_Fo
import matplotlib.pyplot as plt
import os
from scipy.optimize import root
from CoolProp.CoolProp import PropsSI as psi
import scipy.constants as sc
from Functions.Self_defined import check_Fo

shape = 'S'
d = 10e-2
t_0 = 20
t_oo = 80
tau = np.array([0.5, 2]) * 3600
h = 35
lambda_ = 2.2
a = 1.13e-6
c = 780
rho = 2643  # 缺少条件，这里取花岗石的密度

l_c = d/2

Bi = get_Bi(l_c, lambda_, h)
mu = get_mu(Bi, shape)
eta = 0
Fo = get_Fo(tau, l_c, a)
ratio_m_to_0 = theta_to_theta_0_ratio(mu, eta, Fo, shape)
t_m = t_oo + (t_0 - t_oo) * ratio_m_to_0
ratio_Q_m_to_0 = Q_to_Q_0_ratio(mu, Fo, shape)
V = 4/3 * (d/2)**3

# 如果卵石按照正六面体顶点及其中心布置的方式堆放，则每层卵石的数量相等，相邻两层卵石的高度差相等
distance1 = 2*d/np.sqrt(3)  # 同层两相邻卵石之间的距离
distance = distance1/2  # 相邻两层卵石中心平面之间的距离
# 单位高度的层数
layer_number = 1 / distance
# 每层单位面积的卵石数量
n_layer = (1/distance1)**2
# 单位体积的卵石数量为
n = layer_number * n_layer
V_n = n * V

Q_0 = rho * c * V_n * abs(t_0 - t_oo)
Q = ratio_Q_m_to_0 * Q_0

print(f'半小时后，卵石的中心温度为:{t_m[0]:.2f} C，卵石的储热量为：{Q[0]:.0f} J')
print(f'两小时后，卵石的中心温度为:{t_m[1]:.2f} C，卵石的储热量为：{Q[1]:.0f} J')

check_Fo(*Fo)
