import sys
sys.path.append("..")
from Appendix.Appendix4_lambda_ import get_lambda_
from scipy.optimize import root
from Functions.SteadyStateConduction import cylindrical_wall_R

d = 133e-3
t = 400
t_insu = 50
material = '水泥珍珠岩制品'
Phi_l_max = 465

t_m = (t + t_insu) / 2
lambda_m = get_lambda_(material, t_m)
r1 = d / 2


def expressions(p):
    r2, R = p
    expr1 = R - cylindrical_wall_R(r1, r2, lambda_m, 1)
    expr2 = Phi_l_max - (t - t_insu) / R
    return expr1, expr2


guess_value = (r1 + 0.1, 1)
r2, R = root(expressions, guess_value).x
delta = r2 - r1
print(f'delta = {delta:.3f} m')

