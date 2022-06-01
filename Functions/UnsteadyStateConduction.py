import numpy as np
from scipy.special import jv
from scipy.optimize import root


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
    arg = shape_list.index(shape)
    return ratio_list[arg]


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


if __name__ == '__main__':
    Bi_list = np.array([0.1, 0.5, 1.0])
    mu_list = [0.3111, 0.6533, 0.8603]
    shape = 'C'
    Bi = 1.0
    mu = mu(Bi, shape)
    print(mu)
