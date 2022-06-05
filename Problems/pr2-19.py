from Functions.SteadyStateConduction import cylindrical_wall_R
import numpy as np

d = 30e-3
t = 100
t_amb = 20
Phi_l1 = 100   # W/m
Phi_l2 = 50    # W/m, aim

area = np.pi * d

h = Phi_l1 / ((t - t_amb) * area)

lambda_A = 0.5
v_l_A = 3.14e-3
lambda_B = 0.1
v_l_B = 4.0e-3


def find_outer_radius(r_in, area):
    r_out = np.sqrt(area / np.pi + r_in**2)
    return r_out


# 第一种方案，先敷设材料A，再敷设材料B
r_1 = find_outer_radius(d/2, v_l_A)
r_2 = find_outer_radius(r_1, v_l_B)

R_1 = cylindrical_wall_R(d/2, r_1, lambda_A, 1)
R_2 = cylindrical_wall_R(r_1, r_2, lambda_B, 1)
area_out = np.pi * r_2 * 2
R_3 = 1 / (h * area_out)

R = R_1 + R_2 + R_3
Phi_l_A = (t - t_amb) / R

# 第二种方案，先敷设材料B，再敷设材料A
r_1 = find_outer_radius(d/2, v_l_B)
r_2 = find_outer_radius(r_1, v_l_A)

R_1 = cylindrical_wall_R(d/2, r_1, lambda_B, 1)
R_2 = cylindrical_wall_R(r_1, r_2, lambda_A, 1)
area_out = np.pi * r_2 * 2
R_3 = 1 / (h * area_out)

R = R_1 + R_2 + R_3
Phi_l_B = (t - t_amb) / R

if Phi_l_A < Phi_l2 and Phi_l_B < Phi_l2:
    print('两种方案都可行')
elif Phi_l_A < Phi_l2:
    print('先案敷设材料A，再敷设材料B')
elif Phi_l_B < Phi_l2:
    print('先案敷设材料B，再敷设材料A')
else:
    print('两种方案都不可行')
