from Appendix.Appendix4_lambda_ import lambda_

material = '水泥珍沪岩制品'
rho = 300
delta = 120e-3
t1 = 500
t2 = 50
tau = 1 * 3600

t_m = (t1 + t2) / 2
lambda_m = lambda_(material, t_m)
q = lambda_m * (t1 - t2) / delta * tau
print(f'q = {q:.2f} J/m^2')
