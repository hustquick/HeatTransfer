import numpy as np

h_1 = 8700
h_2 = 1800
delta = 1.5e-3
lambda_ = 383

R_1 = 1 / h_1
R_2 = delta / lambda_
R_3 = 1 / h_2
# 尚不清楚，为何以下代码会得到错误的结果
# R_position = np.array([[R_1, '水侧'], [R_2, '管壁'], [R_3, '蒸气侧']])
# ind = np.idxmax(R_position, axis=0)[0]
# print(f'应从{R_position[ind][1]}环节入手，减小其热阻')
R = np.array([R_1, R_2, R_3])
position = ['水侧', '管壁', '蒸气侧']
arg = np.argmax(R)
print(f'应从{position[arg]}环节入手，减小其热阻')
