lambda_ceramics = 1.3
t_max = 1250
lambda_alloy = 25
R_c = 1e-4  # m^2-K/W
t_gas = 1700
h_gas = 1000
t_air = 400
h_air = 500

R_1 = 1 / h_gas
R_2 = delta_ceramics / lambda_ceramics  # 缺少条件：陶瓷层的厚度
R_3 = delta_alloy / lambda_alloy    # 缺少条件：合金层的厚度
R_4 = 1 / h_air
R_total = R_1 + R_2 + R_c + R_3 + R_4

q = (t_gas - t_air) / R_total
t_alloy_max = t_air + q * (R_3 + R_4)
print(f'The maximum temperature of the alloy is {t_alloy_max:.2f}C.')

if t_alloy_max > t_max:
    print('The alloy is too hot to be useful.')
else:
    print('The alloy is safe to use.')

