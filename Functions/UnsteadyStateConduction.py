import numpy as np
from scipy.special import jv
from scipy.optimize import root
from math import erf, erfc


def get_a(lambda_, rho, c):
    '''
    计算热扩散率

    :param lambda_: 导热系数
    :param rho: 密度
    :param c: 比热容
    :return: 热扩散率a
    '''
    return lambda_ / (rho * c)


def get_tau_c(l_c, lambda_, a, h):
    '''
    计算时间常数

    :param l_c: 特征长度
    :param lambda_: 导热系数
    :param a: 热扩散率
    :param h: 换热系数
    :return: 时间常数tau
    '''
    return lambda_ * l_c / (h * a)


def get_Bi(l_c, lambda_, h):
    '''
    计算Bi数

    :param l_c: 特征长度
    :param lambda_: 导热系数
    :param h: 换热系数
    :return: Bi数
    '''
    return l_c * h / lambda_


def get_Fo(tau, l_c, a):
    '''
    计算Fo数

    :param tau: 时间
    :param l_c: 特征长度
    :param a: 热扩散率
    :return: Fo数
    '''
    return a * tau / l_c**2


def theta_to_theta_m_ratio(mu, eta, shape):
    '''
    计算非稳态导热正规状况阶段，任意时刻某处（由eta = x/l_c确定位置）过余温度与中心过余温度之比

    :param mu: 对应形状的超越方程的根，可由mu函数求得
    :param eta: 无量纲位置，由 eta = x/l_c 求得
    :param shape: 形状，可取'P'，'C'或'S'，分别对应平板，圆柱，球
    :return: 过余温度与中心过余温度之比
    '''
    shape_list = ['P', 'C', 'S']
    if shape not in shape_list:
        print('形状指定错误。\n请指定为P（平板）、C（圆柱）、S（球）之一。')
        return None
    if shape == 'P':
        return np.cos(mu * eta)
    elif shape == 'C':
        return jv(0, mu * eta)
    else:
        if eta == 0:
            return 1
        else:
            return np.sin(mu * eta) / (mu * eta)


def theta_to_theta_0_ratio(mu, eta, Fo, shape):
    '''
    计算非稳态导热正规状况阶段，任意时刻某处（由eta = x/l_c确定位置）过余温度与初始过余温度之比

    :param mu: 对应形状的超越方程的根，可由mu函数求得
    :param eta: 无量纲位置，由 eta = x/l_c 求得
    :param Fo: Fo数，表征非稳态过程进行深度的无量纲时间
    :param shape: 形状，可取'P'，'C'或'S'，分别对应平板，圆柱，球
    :return: 过余温度与初始过余温度之比
    '''
    shape_list = ['P', 'C', 'S']
    if shape not in shape_list:
        print('形状指定错误。\n请指定为P（平板）、C（圆柱）、S（球）之一。')
        return None
    arg = shape_list.index(shape)
    A_a = 2 * np.sin(mu) / (mu + np.sin(mu) * np.cos(mu))
    A_b = 2/mu * jv(1, mu) / (jv(0, mu)**2 + jv(1, mu)**2)
    A_c = 2*(np.sin(mu) - mu*np.cos(mu)) / (mu - np.sin(mu)*np.cos(mu))
    A_list = np.array([A_a, A_b, A_c])
    A = A_list[arg]
    part_2 = np.exp(-mu**2*Fo)
    f = theta_to_theta_m_ratio(mu, eta, shape)
    return A*part_2*f


def Q_to_Q_0_ratio(mu, Fo, shape):
    '''
    计算非稳态导热正规状况阶段，物体吸收的总热量与理论可以吸收的最大热量之比

    :param mu: 对应形状的超越方程的根，可由mu函数求得
    :param Fo: Fo数，表征非稳态过程进行深度的无量纲时间
    :param shape: 形状，可取'P'，'C'或'S'，分别对应平板，圆柱，球
    :return: 物体吸收的总热量与理论可以吸收的最大热量之比
    '''
    shape_list = ['P', 'C', 'S']
    if shape not in shape_list:
        print('形状指定错误。\n请指定为P（平板）、C（圆柱）、S（球）之一。')
        return None
    arg = shape_list.index(shape)
    A_a = 2 * np.sin(mu) / (mu + np.sin(mu) * np.cos(mu))
    A_b = 2/mu * jv(1, mu) / (jv(0, mu)**2 + jv(1, mu)**2)
    A_c = 2*(np.sin(mu) - mu*np.cos(mu)) / (mu - np.sin(mu)*np.cos(mu))
    A_list = np.array([A_a, A_b, A_c])
    A = A_list[arg]
    part_2 = np.exp(-mu**2*Fo)
    B_a = np.sin(mu)/mu
    B_b = 2 * jv(1, mu) / mu
    B_c = 3/mu**3*(np.sin(mu) - mu*np.cos(mu))
    B_list = np.array([B_a, B_b, B_c])
    B = B_list[arg]
    return 1 - A*part_2*B


def get_mu(Bi, shape):
    '''
    求解非稳态导热正规状况阶段的mu的值。
    当Bi不为无穷大时，可以通过root函数求解超越方程。
    当Bi为无穷大时，采用工程近似拟合公式计算

    :param Bi: Bi数，固体内部单位导热面积上的导热热阻与单位表面积上的换热热阻之比
    :param shape: 形状，可取'P'，'C'或'S'，分别对应平板，圆柱，球
    :return: mu
    '''
    a_list = [0.4022, 0.1700, 0.0988]
    if Bi <= 0:
        print('Bi数必须大于0，才能计算mu。')
        return None
    shape_list = ['P', 'C', 'S']
    if shape not in shape_list:
        print('形状指定错误。\n请指定为P（平板）、C（圆柱）、S（球）之一。')
        return None
    if shape == 'P':
        if Bi == np.inf:
            a = a_list[0]
            mu = np.sqrt(1 / a)
            return mu
        else:
            mu = root(lambda mu:np.tan(mu)*mu - Bi, 1).x[0]
            return mu
    elif shape == 'C':
        if Bi == np.inf:
            a = a_list[1]
            mu = np.sqrt(1 / a)
            return mu
        else:
            mu = root(lambda mu: mu * jv(1, mu) / jv(0, mu) - Bi, 1).x[0]
            return mu
    else:
        if Bi == np.inf:
            a = a_list[1]
            mu = np.sqrt(1 / a)
            return mu
        else:
            mu = root(lambda mu: 1 - mu / np.tan(mu) - Bi, 1).x[0]
            return mu


def t_x_for_constant_t_w(x, tau, t_0, t_w, a):
    '''
    计算第一类边界条件（壁面温度稳定在某温度）下，指定位置x在时间为tau时的温度

    :param x: 指定的位置
    :param tau: 指定的时间
    :param t_0: 初始温度
    :param t_w: 壁面温度
    :param a: 热扩散系数
    :return: 指定位置x在时间为tau时的温度
    '''
    part = x/(2*np.sqrt(a*tau))
    theta_ratio = erf(part)
    t = t_w + theta_ratio * (t_0 - t_w)
    return t


def q_x_for_constant_t_w(x, tau, t_0, t_w, lambda_, a):
    '''
    计算第一类边界条件（壁面温度稳定在某温度）下，指定位置x在时间为tau时的热流密度

    :param x: 指定的位置
    :param tau: 指定的时间
    :param t_0: 初始温度
    :param t_w: 壁面温度
    :param lambda_: 导热系数
    :param a: 热扩散系数
    :return: 热流密度
    '''
    return (t_w - t_0) * lambda_ / (np.sqrt(np.pi * a * tau)) * np.exp(-x**2/(4*a*tau))


def Q_s_for_constant_t_w(tau, t_0, t_w, lambda_, a):
    '''
    计算第一类边界条件（壁面温度稳定在某温度）下，经过时间tau，物体通过表面单位面积吸收的热量

    :param tau: 传热时间
    :param t_0: 初始温度
    :param t_w: 壁面温度
    :param lambda_: 导热系数
    :param a: 热扩散系数
    :return: 物体通过单位表面积吸收的热量
    '''
    return 2 * lambda_ * np.sqrt(tau/(np.pi*a))*(t_w - t_0)


def t_x_for_constant_q_0(x, tau, t_0, lambda_, a, q_0):
    '''
    计算第二类边界条件（壁面热流密度恒定）下，指定位置x在时间为tau时的温度

    :param x: 指定的位置
    :param tau: 指定的时间
    :param t_0: 初始温度
    :param lambda_: 导热系数
    :param a: 热扩散系数
    :param q_0: 壁面热流密度
    :return: 指定位置x在时间为tau时的温度
    '''
    part1 = x/(2*np.sqrt(a*tau))
    part2 = 2 * q_0 * np.sqrt(a*tau/np.pi) / lambda_
    delta_t = part2 * np.exp(-part1**2) - q_0 * x / lambda_ * erfc(part1)
    t = t_0 + delta_t
    return t


def t_x_for_constant_h(x, tau, t_0, t_oo, lambda_, a, h):
    '''
    计算第三类边界条件（已知壁面换热系数）下，指定位置x在时间为tau时的温度

    :param x: 指定的位置
    :param tau: 指定的时间
    :param t_0: 初始温度
    :param t_oo: 流体温度
    :param lambda_: 导热系数
    :param a: 热扩散系数
    :param h: 表面传热系数
    :return: 指定位置x在时间为tau时的温度
    '''
    part1 = x/(2*np.sqrt(a*tau))
    part2 = h * x / lambda_ + h**2*a*tau / lambda_**2
    part3 = part1 + h * np.sqrt(a * tau) / lambda_
    theta_ratio = erfc(part1) - np.exp(part2)*erfc(part3)
    t = t_0 + theta_ratio * (t_oo - t_0)
    return t


if __name__ == '__main__':
    print()
