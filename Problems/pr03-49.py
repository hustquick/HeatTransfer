import numpy as np
import sys
sys.path.append("..")
from Functions.UnsteadyStateConduction import q_x_for_constant_t_w, get_mu, get_Bi, get_Fo, get_a

# 人对温度的感知由热流密度决定，比较二者的热流密度即可
# 而在接触面两边，人体皮肤中的热流密度等于触摸物中的热流密度
# 只需要比较两种情况下触摸物表面热流密度的相对大小即可
# 由于短时间内皮肤表面温度不会下降太多，可以把该问题看做半无限大平板第一类边界条件下的热流密度的求解问题
t_0 = 20
rho_1 = 545
lambda_1 = 0.17
c_1 = 2385
rho_2 = 7820
lambda_2 = 18
c_2 = 460

a_1 = get_a(lambda_1, rho_1, c_1)
a_2 = get_a(lambda_2, rho_2, c_2)

# # 假定人体皮肤的温度为37.5°C，人体在0.2s后感应出冷热
# t_w = 37.5
# tau = 0.2
#
#
# q_1 = q_x_for_constant_t_w(0, tau, t_0, t_w, lambda_1, a_1)
# q_2 = q_x_for_constant_t_w(0, tau, t_0, t_w, lambda_2, a_2)
# ratio = q_1 / q_2

# 根据式3-38， 对于x=0，两种情况下触摸物表面热流密度之比ratio为
ratio = lambda_1/lambda_2 * np.sqrt(a_2/a_1)
if 0 < ratio < 1:
    print('钢制家具感觉更冷一些')
elif ratio >= 1:
    print('木制家具感觉更冷一些')
else:
    print('计算错误')
