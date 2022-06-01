import numpy as np
from scipy.special import jv
from scipy.optimize import root
from math import erf, erfc


def tau_c(l_c, rho, c, h):
    return rho * c * l_c / h


def Bi(l_c, lambda_, h):
    return l_c * h / lambda_


def Fo(l_c, rho, c, lambda_, tau):
    return lambda_ * tau / (rho * c * l_c ** 2)


def theta_to_theta_m_ratio(mu, eta, shape):
    shape_list = ['P', 'C', 'S']
    ratio_list = [np.cos(mu * eta), jv(0, mu * eta), np.sin(mu * eta) / (mu * eta)]
    if shape not in shape_list:
        print('形状指定错误。\n请指定为P（平板）、C（圆柱）、S（球）之一。')
        return None
    if shape == 'P':
        return np.cos(mu * eta)
    elif shape == 'C':
        return jv(0, mu * eta)
    else:
        return np.sin(mu * eta) / (mu * eta)


def theta_to_theta_0_ratio(mu, eta, Fo, shape):
    shape_list = ['P', 'C', 'S']
    if shape not in shape_list:
        print('形状指定错误。\n请指定为P（平板）、C（圆柱）、S（球）之一。')
        return None
    arg = shape_list.index(shape)
    part_1a = 2 * np.sin(mu) / (mu + np.sin(mu) * np.cos(mu))
    part_1b = 2/mu * jv(1, mu) / (jv(0, mu)**2 + jv(1, mu)**2)
    part_1c = 2*(np.sin(mu) - mu*np.cos(mu)) / (mu - np.sin(mu))
    part_1_list = np.array([part_1a, part_1b, part_1c])
    part_1 = part_1_list[arg]
    part_2 = np.exp(-mu**2*Fo)
    part_3 = theta_to_theta_m_ratio(mu, eta, shape)
    return part_1*part_2*part_3


def mu(Bi, shape):
    shape_list = ['P', 'C', 'S']
    if shape not in shape_list:
        print('形状指定错误。\n请指定为P（平板）、C（圆柱）、S（球）之一。')
        return None
    if shape == 'P':
        mu = root(lambda mu:np.tan(mu)*mu - Bi, 1).x[0]
    elif shape == 'C':
        mu = root(lambda mu: mu * jv(1, mu) / jv(0, mu) - Bi, 1).x[0]
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
    :return:
    '''
    part = x/(2*np.sqrt(a*tau))
    theta_ratio = erf(part)
    t = t_w + theta_ratio * (t_0 - t_w)
    return t


def t_x_for_constant_q_0(x, tau, t_0, t_w, lambda_, a, q_0):
    '''
    计算第二类边界条件（壁面热流密度恒定）下，指定位置x在时间为tau时的温度

    :param x: 指定的位置
    :param tau: 指定的时间
    :param t_0: 初始温度
    :param t_w: 壁面温度
    :param lambda_: 导热系数
    :param a: 热扩散系数
    :param q_0: 壁面热流密度
    :return:
    '''
    part1 = x/(2*np.sqrt(a*tau))
    part2 = 2 * q_0 * np.sqrt(a*tau/np.pi) / lambda_
    theta_ratio = part2 * np.exp(-part1**2) - q_0 * x / lambda_ * erfc(part1)
    t = t_w + theta_ratio * (t_0 - t_w)
    return t


def t_x_for_constant_h(x, tau, t_0, t_w, lambda_, a, h):
    '''
    计算第二类边界条件（壁面热流密度恒定）下，指定位置x在时间为tau时的温度

    :param x: 指定的位置
    :param tau: 指定的时间
    :param t_0: 初始温度
    :param t_w: 壁面温度
    :param lambda_: 导热系数
    :param a: 热扩散系数
    :param h: 表面传热系数
    :return:
    '''
    part1 = x/(2*np.sqrt(a*tau))
    part2 = h * x / lambda_ + h**2*a*tau / lambda_**2
    part3 = part1 + h * np.sqrt(a * tau) / lambda_
    theta_ratio = erfc(part1) - np.exp(part2)*erfc(part3)
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
    :return:
    '''
    return (t_w - t_0) * lambda_ / (np.sqrt(np.pi * a * tau)) * np.exp(-x**2/(4*a*tau))


if __name__ == '__main__':
    shape = ['P', 'C']
    d = 600e-3
    l = 1000e-3
    t_0 = 30
    t_oo = 1300
    tau = 4 * 3600
    h = 232
    lambda_ = 40.5
    a = 0.625e-5

    l_c_2 = d / 2
    Bi_2 = h * l_c_2 / lambda_
    Fo_2 = a * tau / l_c_2 ** 2
    mu_2 = mu(Bi_2, shape[1])
    eta_2 = 0
    ratio_to_0_2 = theta_to_theta_0_ratio(mu_2, eta_2, Fo_2, shape[1])
    print(ratio_to_0_2)
