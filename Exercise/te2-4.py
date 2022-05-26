from scipy.optimize import root

delta_ratio_A_B = 2
lambda_A = 0.08
lambda_B = 0.05
t_f1 = 400
h_1 = 50
t_w = 50
t_f2 = 25
h_2 = 9.5

q = h_2 * (t_w - t_f2)


def expressions(p):
    delta_A, delta_B, R_total = p
    expr1 = delta_A - delta_B * delta_ratio_A_B
    expr2 = R_total - 1/h_1 - 1/h_2 - delta_A/lambda_A - delta_B/lambda_B
    expr3 = q - (t_f1 - t_f2) / R_total
    return expr1, expr2, expr3


guess_value = (0.02, 0.01, 1)
delta_A, delta_B, R_total = root(expressions, guess_value).x
print(f'delta_A = {delta_A:.3f} m')
print(f'delta_B = {delta_B:.3f} m')
