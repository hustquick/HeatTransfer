import scipy.constants as const

epsilon = 0.8
t = 27

T = const.convert_temperature(t, 'C', 'K')

q = const.sigma * T**4
print(f"单位时间内单位面积钢板上所发出的辐射能为：{q:.2f} W/m^2")
