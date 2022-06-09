import numpy as np
import scipy.constants as sc

d = 583e-3
t_w = 48
t_f = 23
h = 3.42
epsilon = 0.9

T_w = sc.convert_temperature(t_w, 'C', 'K')
T_f = sc.convert_temperature(t_f, 'C', 'K')

q_conv = np.pi * d * h * (t_w - t_f)
q_radi = epsilon * sc.sigma * (np.pi * d) * (T_w ** 4 - T_f ** 4)
q_tot = q_conv + q_radi
print(f"管道的总散热量为：{q_tot:.2f} W/m")
