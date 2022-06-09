from Functions.UnsteadyStateConduction import t_x_for_constant_t_w
import scipy.constants as sc
from scipy.optimize import root
import numpy as np

t_0 = 10    # 原地表温度，能否作为原地表以下的土壤的统一温度，有疑问
t_w = -15
tau = 45 * sc.day
t = 0
c = 1840
rho = 2050
lambda_ = 0.52

a = lambda_ / (rho * c)

guess_values = np.ones(1)
x = root(lambda x: t - t_x_for_constant_t_w(x, tau, t_0, t_w, a), guess_values).x[0]
print(f'x = {x:.2f} m')
