from Functions.SteadyStateConduction import fin_tip_efficiency
import numpy as np
from scipy.integrate import solve_bvp
import matplotlib.pyplot as plt
import os
from Functions.Self_defined import find_nearest, save_pdf

h_i, h_o = 2, 10
d_i, d_o = 25e-3, 30e-3
H = 90e-3
t_f = 15
t_w = 70
lambda_ = 1.3  # 缺少条件，课本并未给出，这里取黏土的导热系数
t_search = 35

r_i, r_o = d_i / 2, d_o / 2
delta = r_o - r_i
H_p = H + delta/2

perimeter = np.pi * d_i + np.pi * d_o
A_c = np.pi * (r_o**2 - r_i**2)
efficiency = fin_tip_efficiency(H_p, perimeter, A_c, lambda_, 1)
area_i = np.pi * d_i * H_p
area_o = np.pi * d_o * H_p
Phi = efficiency * (h_i * area_i + h_o * area_o) * (t_w - t_f)
print(f'手柄传递的热流量为: {Phi:.2f} W')

# # 用scipy的bvp工具求解具体的温度分布
# 记y = t'(x)
# 定义t的导数函数，返回其1阶导数和2阶导数
N = 100


def derivative(x, t):
    k = 4 * (d_o*h_o + d_i*h_i) / (lambda_ * (d_o**2 - d_i**2))
    return np.vstack((t[1], k * (t[0] - t_f)))


# 定义边界条件，t(0) = t_water, t'(L/2) = 0
# 边界条件函数的t_a和t_b参数为边界条件的起始和终止点
def bc(t_a, t_b):
    return np.array([t_a[0] - t_w, t_b[1]])


x = np.linspace(0, H, N)
t = np.zeros((2, x.size))
t[0, 0] = t_w
result = solve_bvp(derivative, bc, x, t)

x_plot = np.linspace(0, H_p, N)
t_plot = result.sol(x_plot)[0]
plt.plot(x_plot, t_plot)
plt.grid()
plt.xlabel('$x(\mathrm{m})$')
plt.ylabel('$t(\mathrm{^\circ C})$')
name = os.path.basename(__file__).split(".")[0]
save_pdf(name, plt)

arg = find_nearest(t_plot, t_search)
print(f'温度为{t_search}°C的位置离手柄与锅体相接部分{x_plot[arg]:.3f} m')
