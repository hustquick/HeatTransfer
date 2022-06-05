from scipy.optimize import root

delta_s = 1e-3  # 基板的厚度
delta_f = 0.2e-3    # 薄膜的厚度
t_f = 20
h = 40
t_1 = 30
t_0 = 60
lambda_f = 0.02
lambda_s = 0.06

R_1 = 1 / h
R_2 = delta_f / lambda_f


def expressions(p):
    q_1, t_2 = p
    xpr1 = q_1 - h * (t_2 - t_f)
    xpr2 = q_1 - (t_0 - t_2) * lambda_f / delta_f
    return [xpr1, xpr2]


guess_values = [1, t_0 - 10]
q_1, t_2 = root(expressions, guess_values).x
q_2 = (t_0 - t_1) * lambda_s / delta_s
# 在薄膜与基板的接触面处能量守恒
q = q_1 + q_2
print(f'q = {q:.2f} W/m^2')
