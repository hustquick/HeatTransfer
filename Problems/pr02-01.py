from scipy.optimize import root

t_boiler = 111
q = 42400
delta = 3e-3
lambda_ = 1

t = root(lambda t: q - lambda_ * (t - t_boiler) / delta,
         t_boiler + 10).x[0]
print(f't = {t:.2f}degC')
