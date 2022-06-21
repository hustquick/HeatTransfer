import numpy as np

h_1 = 8700
h_2 = 1800
delta = 1.5e-3
lambda_ = 383

R_1 = 1 / h_1
R_2 = delta / lambda_
R_3 = 1 / h_2
# 以下代码会得到错误的结果，是因为将R_position转换为数组类型时，R_1, R_2, R_3都被转换成了字符串。
# 可以通过R_position_numpy = np.array(R_position)查看结果
# R_position = np.array([[R_1, '水侧'], [R_2, '管壁'], [R_3, '蒸气侧']])
# idx = np.argmax(R_position, axis=0)[0]
# print(f'应从{R_position[idx][1]}环节入手，减小其热阻')
R = np.array([R_1, R_2, R_3])
position = ['水侧', '管壁', '蒸气侧']
arg = np.argmax(R)
print(f'应从{position[arg]}环节入手，减小其热阻')
