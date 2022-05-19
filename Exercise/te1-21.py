h_1 = 95
delta = 2.5e-3
lambda_ = 46.5
h_2 = 5800

R_1 = 1 / h_1
R_2 = 1 / h_2
R_3 = delta / lambda_

print(f'R_1 = {R_1:.2e} K/W, R_2 = {R_2:.2e} K/W, R_3 = {R_3:.2e} K/W')

R = R_1 + R_2 + R_3
h = 1 / R
print(f'h = {h:.2f} K/W')

position = {R_1: '气侧', R_2: '热壁', R_3: '水侧'}
max_resistance_position = position[max(position.keys())]
print(f'为了强化这一传热过程，应首先从{max_resistance_position}环节着手')
