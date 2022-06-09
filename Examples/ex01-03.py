import scipy.constants as sc

epsilon = 0.8
t = 27

T = sc.convert_temperature(t, 'C', 'K')

q = sc.sigma * T ** 4
print(f"单位时间内单位面积钢板上所发出的辐射能为：{q:.2f} W/m^2")
