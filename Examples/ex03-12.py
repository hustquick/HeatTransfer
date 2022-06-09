from Functions.UnsteadyStateConduction import t_x_for_constant_t_w
from scipy.optimize import root, minimize
import numpy as np
from math import erf
from CoolProp.CoolProp import PropsSI as psi
import scipy.constants as sc

T_oo = 303
f = 5
v = 20
d = 0.9e-3
rho = 8332
c_p = 188
Lambda_ = 51

# 涉及到对流换热公式，后续再求解。
