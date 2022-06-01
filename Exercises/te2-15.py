from Functions.SteadyStateConduction import cylindrical_wall_R
import Appendix4_lambda_ as ap4
import sympy as sp
import numpy as np

d_1 = 50e-3
delta_1 = 40e-3
lambda_1 = 0.11
delta_2 = 45e-3
lambda_2 = 0.12
t_o = 50
t_i = 400
material1 = '矿渣棉'
material2 = '粉煤灰泡沫砖'

idx1 = ap4.material_list.index(material1)
idx2 = ap4.material_list.index(material2)
t_12_max = min(ap4.t_max[idx1], ap4.t_max[idx2])

R_1 = cylindrical_wall_R(d_1/2, d_1/2+delta_1, lambda_1, 1)
R_2 = cylindrical_wall_R(d_1/2+delta_1, d_1/2+delta_1+delta_2, lambda_2, 1)
R = R_1 + R_2
q = (t_i - t_o) / R
t_12 = t_o + q * R_2
if t_12 > t_12_max:
    print('矿渣棉与煤灰泡沫砖交界界面处的温度超过允许值')
else:
    print('矿渣棉与煤灰泡沫砖交界界面处的温度不超过允许值')

R_2, delta_2 = sp.symbols('R_2 delta_2')
r2 = d_1/2 + delta_1 + delta_2
r1 = d_1/2 + delta_1
length = 1
R_2 = sp.log(r2/r1) / (2*np.pi*lambda_2*length)
dR_2_ddelta_2 = sp.diff(R_2, delta_2).subs(delta_2, 0.045)
if dR_2_ddelta_2 > 0:
    print('增加煤灰泡沫砖的厚度会导致热损失下降')
else:
    print('增加煤灰泡沫砖的厚度会导致热损失增加')
