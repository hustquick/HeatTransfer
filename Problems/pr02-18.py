import sys
sys.path.append("..")
from Functions.SteadyStateConduction import cylindrical_wall_R

d = 100e-3
lambda_1 = 0.05
lambda_2 = 0.08
delta_1 = delta_2 = 75e-3

R_1i = cylindrical_wall_R(d/2, d/2+delta_1, lambda_1, 1)
R_1o = cylindrical_wall_R(d/2+delta_1, d/2+delta_1+delta_2, lambda_1, 1)
R_2i = cylindrical_wall_R(d/2, d/2+delta_2, lambda_2, 1)
R_2o = cylindrical_wall_R(d/2+delta_2, d/2+delta_2+delta_1, lambda_2, 1)

R_1 = R_1i + R_1o
R_2 = R_2i + R_2o

if R_1 > R_2:
    print(f'导热系数小的材料紧贴管壁保温效果更好')
else:
    print(f'导热系数大的材料紧贴管壁保温效果更好')
