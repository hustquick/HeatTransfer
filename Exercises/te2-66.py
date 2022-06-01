import numpy as np

H_1 = 3
H_2 = 2
d = 500e-3
lambda_ = 1
t_s = 0
t_w = 4
length = 1

if H_1 > 2 * d:
    S_1 = 2 * np.pi * length / np.log(4 * H_1/d)
else:
    print('课本无对应公式')

Phi_1 = lambda_ * S_1 * (t_w - t_s)
print(f'每米管道的散热量为： {Phi_1:.2f} W')

# 结冰后，地下深度为1 m的土壤层的温度跟原来相同，为0摄氏度
if H_2 > 2 * d:
    S_2 = 2 * np.pi * length / np.log(4 * H_2/d)
else:
    print('课本无对应公式')

Phi_2 = lambda_ * S_2 * (t_w - t_s)
print(f'结冰后，每米管道的散热量为： {Phi_2:.2f} W')
