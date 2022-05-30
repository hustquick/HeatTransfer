import numpy as np

y_list = np.array([51.2, 53.3, 54.4, 56.9, 59.5, 61.6])
x_list = np.array([5, 25, 40, 60, 75, 95])*1e-3

lambda_ = 42.8
x = 50e-3   # 题目错误，应该是50e-3
result1 = np.polyfit(x_list[:3], y_list[:3], 1)
t_50_l = np.poly1d(result1)(x)
result2 = np.polyfit(x_list[3:], y_list[3:], 1)
t_50_r = np.poly1d(result2)(x)
Delta_T = t_50_r - t_50_l

q = lambda_ * (result1[1] + result2[1]) / 2
R_c = Delta_T / q
print(f'接触热阻为：{R_c:.2e} m^2-K/W')
