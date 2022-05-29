import numpy as np


def plate_wall_R(delta, lambda_, area):
    return delta / (lambda_ * area)


def plate_wall_Delta_T_with_heat_source(delta, lambda_, h, q_dot):
    return q_dot * delta**2 / (8 * lambda_) + q_dot * delta / (2 * h)


def cylindrical_wall_R(r1, r2, lambda_, length):
    return np.log(r2/r1) / (2*np.pi*lambda_*length)


def cylinder_Delta_T_with_heat_source(r, lambda_, q_dot):
    return q_dot * r**2 / (4 * lambda_)


def spherical_wall_R(r1, r2, lambda_):
    return (1/r1 - 1/r2) / (4*np.pi*lambda_)


def sphere_Delta_T_with_heat_source(r, lambda_, q_dot):
    return q_dot * r**2 / (6 * lambda_)


def fin_tip_m(perimeter, A_c, lambda_, h):
    return np.sqrt(h * perimeter / (lambda_ * A_c))


def fin_tip_efficiency(H, perimeter, A_c, lambda_, h):
    '''

    :param H: 肋片的高度
    :param perimeter: 肋片的周长
    :param A_c: 肋片的截面积
    :param lambda_: 肋片的导热系数
    :param h: 肋片的对流传热系数
    :return: 计算肋片效率的方法
    '''
    m = fin_tip_m(perimeter, A_c, lambda_, h)
    # print(m*H)
    return np.tanh(m*H) / (m*H)


def fin_tip_R(H, perimeter, A_c, lambda_, h):
    m = fin_tip_m(perimeter, A_c, lambda_, h)
    # print(H)
    return 1 / np.sqrt(lambda_ * A_c * h * perimeter) / np.tanh(m*H)


def fin_tip_efficiency2(H, A_L, lambda_, h):
    """可应用于环肋的效率计算
    :param H: 肋片的高度
    :param A_L: 肋片的纵剖面积
    :param lambda_: 肋片的导热系数
    :param h: 肋片的对流传热系数
    :return: 另一种计算肋片效率的方法
    """
    mH = np.sqrt(2* h / (lambda_ * A_L)) * H**(3/2)
    print(f'mH={mH}')
    return np.tanh(mH) / mH


def fin_tip_Delta_T_ratio(H, perimeter, A_c, lambda_, h):
    '''

    :param H: 肋片的高度
    :param perimeter: 肋片的周长
    :param A_c: 肋片的截面积
    :param lambda_: 肋片的导热系数
    :param h: 肋片的对流传热系数
    :return: 肋片的底端温差与顶端温差之比
    '''
    m = fin_tip_m(perimeter, A_c, lambda_, h)
    # print(f'm={m}')
    # print(f'mH={m*H}')
    return 1 / np.cosh(m*H)


def overall_fin_surface_efficiency(A_f, A_r, eta_f):
    '''

    :param A_f: 肋片的表面积
    :param A_r: 两个肋片之间的根部表面积
    :param eta_f: 肋片的效率
    :return: 肋片的整体效率
    '''
    return (A_r + eta_f * A_f) / (A_r + A_f)
