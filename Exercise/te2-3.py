delta = 20e-3
lambda_ = 1.3
q = 1500
lambda_insu = 0.08
t_in = 750
t_out = 55

R_1 = delta / lambda_
R_total = (t_in - t_out) / q
R_2 = R_total - R_1
delta_insu = lambda_insu * R_2
print(f'保温层的厚度为 {delta_insu*1000:.0f} mm')
