import numpy as np
from scipy.optimize import root
import sys
sys.path.append("..")
from Functions.UnsteadyStateConduction import theta_to_theta_0_ratio, get_a, get_mu, get_Bi, get_Fo
import matplotlib.pyplot as plt
from scipy.integrate import solve_bvp

r = 2e-2
dt_dtau = -0.5
lambda_ = 43
a = 1.2e-5

dPhi_dr = - 2 * np.pi * lambda_ * r / a * dt_dtau
print(f'dPhi_dr = {dPhi_dr:.0f} W/m')
if dPhi_dr > 0:
    print('方向由圆柱的中心指向外侧')
else:
    print('方向由圆柱的外侧指向中心')
