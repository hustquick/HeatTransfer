from scipy.optimize import fsolve
import numpy as np

d_i = 8.25e-3       # 合金管内径
d_o = 9.27e-3       # 合金管外径
distance = 17.5e-3  # 合金管距离
phi_dot = 8.73e8    # 铀棒热功率
T_f = 400           # 冷却水温度
h_o = 10000         # 合金管外壁换热系数
h_ct = 6000         # 合金管内壁换热系数

T_list1 = [500, 600, 800]   # 温度列表1
lambda_zir_list1 = [16.2, 17.2, 19.2]   # 合金管导热系数列表
T_list2 = [1000, 1500, 2000]    # 温度列表2
lambda_u_list2 = [3.9, 2.6, 2.3]    # 铀棒导热系数列表


def lambda_zir(T):
    return np.interp(T, T_list1, lambda_zir_list1)


def lambda_u(T):
    return np.interp(T, T_list2, lambda_u_list2)


A_i = np.pi * d_i
A_o = np.pi * d_o
Q = phi_dot * np.pi * d_i**2 / 4    # 铀棒热功率


def equations(p):
    """ T_u, T_i, T_o都是未知数，有三个关于它们的方程，因此可以求解方程组。
        其中，lambda_zir是关于(T_i + T_o) / 2的函数。
    """
    T_u, T_i, T_o = p
    err1 = Q - h_ct * A_i * (T_u - T_i)
    err2 = Q - h_o * A_o * (T_o - T_f)
    err3 = Q - 2 * np.pi * lambda_zir((T_i + T_o) / 2) * (T_i - T_o) \
           / np.log(d_o / d_i)
    return err1, err2, err3


guess_value = np.array([1000, 900, 800])
T_u, T_i, T_o = fsolve(equations, guess_value)


# def eqation2(p):
#     T_max = p
#     err = T_max - 1 / 4 * phi_dot * (d_i**2 / 4) / lambda_u((T_max + T_u) / 2) - T_u
#     return err


guess_value2 = T_u + 100
T_max = fsolve(lambda T_max: T_max - 1 / 4 * phi_dot * (d_i**2 / 4) / lambda_u((T_max + T_u) / 2) - T_u,
               guess_value2)[0]
print(f"稳态过程中，铀棒的最高温度为{T_max:.0f} K")
