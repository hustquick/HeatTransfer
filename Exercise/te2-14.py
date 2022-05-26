from functions import cylindrical_wall_R
from Appendix4_lambda_ import lambda_
from scipy.optimize import root

d = 100e-3
density = 20
t_o = 400
t_insu = 50
Phi = 163
material = '超细玻璃棉毡、管'
lambda_insu = lambda_(material, (t_o+t_insu)/2)
R_insu = (t_o - t_insu) / Phi
lambda_insu = lambda_(material, (t_o + t_insu)/2)

guess_value = d
delta = root(lambda delta: R_insu - cylindrical_wall_R(d/2, d/2 + delta, lambda_insu, 1), guess_value).x[0]
print(f'delta = {delta:.3f} m')
