import scipy.constants as sc

delta = 0.1
lambda_ = 17.5
t_w1 = 27
t_w2 = 127

T_w1 = sc.convert_temperature(t_w1, 'C', 'K')
T_w2 = sc.convert_temperature(t_w2, 'C', 'K')
q = sc.sigma * (T_w2**4 - T_w1**4)
t_w3 = t_w2 + q * delta / lambda_
print(f"t_w3 = {t_w3:.2f}degC")
