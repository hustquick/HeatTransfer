import numpy as np
from functions import fin_tip_efficiency2
from scipy.integrate import odeint, solve_bvp
import matplotlib.pyplot as plt

lambda_ = 177
delta = 6e-3
L = 200e-3
I = 800 # W/m^2
t_water = 60

# 将问题看成厚度为 2*delta，高度为 L/2 的等截面直肋的换热分析，该换热为等热流密度换热
# 对厚度为dx的截面微元块分析，可知微分公式为：-lambda_ * delta * t''(x) = I

# 试试用scipy的bvp工具求解
# 记y = t'(x)
# 定义t的导数函数，返回其1阶导数和2阶导数
N = 100


def derivative(x, t):
    return np.vstack((t[1], - I / (lambda_ * delta) * np.ones(len(t[1]))))


# 定义边界条件，t(0) = t_water, t'(L/2) = 0
# 边界条件函数的t_a和t_b参数为边界条件的起始和终止点
def bc(t_a, t_b):
    return np.array([t_a[0] - t_water, t_b[1]])


x = np.linspace(0, L/2, N)
t = np.zeros((2, x.size))
t[0, 0] = t_water
result = solve_bvp(derivative, bc, x, t)

x_plot = np.linspace(0, L/2, N)
t_plot = result.sol(x_plot)[0]
plt.plot(x_plot, t_plot)
plt.grid()
plt.xlabel('x(m)')
plt.ylabel('t(°C)')
plt.savefig('./te2-58.pdf')
plt.show()
print(f'最大温度为{t_plot[-1]:.2f} C')
