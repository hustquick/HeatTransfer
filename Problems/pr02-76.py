import scipy.constants as sc
import numpy as np
import sys
sys.path.append("..")
from Functions.SteadyStateConduction import sphere_Delta_T_with_heat_source
import os

Q = 4000  # J/kg
time = 1 * sc.day
rho = 840
lambda_ = 0.5
h = 6
d = 80e-3
t_oo = 5
v = 0.6

Q_v = Q * rho
Phi = Q_v / time

Delta_T = sphere_Delta_T_with_heat_source(d/2, lambda_, Phi)
surface_area = np.pi * d**2
V = 4 / 3 * np.pi * (d/2)**3
t_r = t_oo + Phi * V / (h * surface_area)
t_0 = t_r + Delta_T
print(f'苹果中心温度为{t_0:.2f}degC')
print(f'苹果表面温度为{t_r:.2f}degC')

# # 也可以用scipy的bvp工具求解
# # 记y = t'(r)
# # 定义t的导数函数，返回其1阶导数和2阶导数
# N = 100
#
#
# def derivative(r, t):
#     return np.vstack((t[1], - 2/r * t[1] - Phi/lambda_))
#
#
# # 定义边界条件，t(0) = t_water, t'(L/2) = 0
# # 边界条件函数的t_a和t_b参数为边界条件的起始和终止点
# def bc(t_a, t_b):
#     return np.array([t_a[1], lambda_ * t_b[1] + h * (t_b[0] - t_oo)])
#
#
# r = np.linspace(0.0001, d/2, N)
# t = np.zeros((2, r.size))
# t[0, 0] = t_oo
# result = solve_bvp(derivative, bc, r, t)
#
# x_plot = np.linspace(0.0001, d/2, N)
# t_plot = result.sol(x_plot)[0]
# plt.plot(x_plot, t_plot)
# plt.grid()
# plt.xlabel('r(m)')
# plt.ylabel('t(°C)')
# name = os.path.basename(__file__).split(".")[0]
# plt.savefig(f'./{name}.pdf')
# plt.show()
# print(f'苹果中心温度为{t_plot[0]:.2f}degC')
# print(f'苹果表面温度为{t_plot[-1]:.2f}degC')
