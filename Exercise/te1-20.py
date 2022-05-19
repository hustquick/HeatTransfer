import scipy.constants as sc
from scipy.optimize import fsolve

r = 0.5
epsilon = 0.8
Q = 175
T_a = 2.7

A = 4 * sc.pi * r ** 2

guess_T = T_a + 100
T = fsolve(lambda T: Q - epsilon * sc.sigma * (T**4 - T_a**4), guess_T)[0]
print(f'其外表面温度为{T:.2f} K')
