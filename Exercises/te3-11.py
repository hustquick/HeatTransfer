import numpy as np
from scipy.optimize import root

m_l = 3.45e-3
c = 460
R_l = 3.63e-2
I = 8

dT_dtau = I**2 * R_l / (m_l * c)
print(f'导线刚通电瞬间的温升率为：{dT_dtau:.2f} C/s')
