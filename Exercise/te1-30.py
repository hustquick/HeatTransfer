t_h, t_c = 20, 0
delta = 0.08
t_f1 = 100
h_1 = 200

q = h_1 * (t_f1 - t_h)
lambda_ = (q * delta) / (t_h - t_c)
print(f"导热系数为：{lambda_} W/m^2.K")
