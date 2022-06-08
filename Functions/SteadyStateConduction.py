import numpy as np


def plate_wall_R(delta, lambda_, area):
    '''
    计算平板的热阻

    :param delta: 壁厚
    :param lambda_: 导热系数
    :param area: 平板的一面的换热面积
    :return: 平板的热阻
    '''
    return delta / (lambda_ * area)


def plate_wall_Delta_T_with_heat_source(delta, lambda_, h, q_dot):
    '''
    计算具有内热源的平板壁的最大温差

    :param delta: 壁厚
    :param lambda_: 导热系数
    :param h: 表面换热系数
    :param q_dot: 内热源单位体积发热功率
    :return: 平板壁的中心温度与外壁温度之差
    '''
    return q_dot * delta**2 / (8 * lambda_) + q_dot * delta / (2 * h)


def cylindrical_wall_R(r1, r2, lambda_, length):
    '''
    计算圆筒壁的热阻

    :param r1: 圆筒的内半径
    :param r2: 圆筒的外半径
    :param lambda_: 导热系数
    :param length: 圆筒的长度
    :return: 圆筒壁的热阻
    '''
    return np.log(r2/r1) / (2*np.pi*lambda_*length)


def cylinder_Delta_T_with_heat_source(r, lambda_, q_dot):
    '''
    计算具有内热源的圆柱的最大温差

    :param r: 圆柱的半径
    :param lambda_: 导热系数
    :param q_dot: 内热源单位体积发热功率
    :return: 圆柱的中心温度与外壁温度之差
    '''
    return q_dot * r**2 / (4 * lambda_)


def spherical_wall_R(r1, r2, lambda_):
    '''
    计算球壳的热阻

    :param r1: 球壳的内半径
    :param r2: 球壳的外半径
    :param lambda_: 导热系数
    :return: 球壳的热阻
    '''
    return (1/r1 - 1/r2) / (4*np.pi*lambda_)


def sphere_Delta_T_with_heat_source(r, lambda_, q_dot):
    '''
    计算具有内热源的球体的最大温差

    :param r: 球的半径
    :param lambda_: 导热系数
    :param q_dot: 内热源单位体积发热功率
    :return: 球的中心温度与外壁温度之差
    '''
    return q_dot * r**2 / (6 * lambda_)


def fin_tip_m(perimeter, A_c, lambda_, h):
    '''
    计算肋片的m值

    :param perimeter: 肋片横截面的周长
    :param A_c: 肋片横截面的面积
    :param lambda_: 肋片的导热系数
    :param h: 肋片的表面换热系数
    :return: 肋片的m值
    '''
    return np.sqrt(h * perimeter / (lambda_ * A_c))


def fin_tip_efficiency(H, perimeter, A_c, lambda_, h):
    '''
    计算等截面肋片的效率

    :param H: 肋片的高度
    :param perimeter: 肋片横截面的周长
    :param A_c: 肋片横截面的面积
    :param lambda_: 肋片的导热系数
    :param h: 肋片的表面传热系数
    :return: 肋片的效率
    '''
    m = fin_tip_m(perimeter, A_c, lambda_, h)
    # print(f'mH = {m*H}')
    return np.tanh(m*H) / (m*H)


def fin_tip_R(H, perimeter, A_c, lambda_, h):
    '''
    计算肋片的热阻

    :param H: 肋片的高度
    :param perimeter: 肋片横截面的周长
    :param A_c: 肋片横截面的面积
    :param lambda_: 肋片的导热系数
    :param h: 肋片的表面传热系数
    :return: 肋片的热阻
    '''
    m = fin_tip_m(perimeter, A_c, lambda_, h)
    # print(f'H = {H}')
    return 1 / np.sqrt(lambda_ * A_c * h * perimeter) / np.tanh(m*H)


def fin_tip_efficiency2(H, A_L, lambda_, h):
    """
    计算肋片的效率，特别应用于环肋的效率计算

    :param H: 肋片的高度
    :param A_L: 肋片的纵剖面积
    :param lambda_: 肋片的导热系数
    :param h: 肋片的表面传热系数
    :return: 肋片效率
    """
    mH = np.sqrt(2 * h / (lambda_ * A_L)) * H**(3/2)
    print(f'mH = {mH}')
    return np.tanh(mH) / mH


def fin_tip_Delta_T_ratio(H, perimeter, A_c, lambda_, h):
    '''
    计算肋片的顶端温差与底端温差之比

    :param H: 肋片的高度
    :param perimeter: 肋片的周长
    :param A_c: 肋片的截面积
    :param lambda_: 肋片的导热系数
    :param h: 肋片的对流传热系数
    :return: 肋片的顶端温差与底端温差之比
    '''
    m = fin_tip_m(perimeter, A_c, lambda_, h)
    # print(f'm = {m}')
    # print(f'mH = {m*H}')
    return 1 / np.cosh(m*H)


def overall_fin_surface_efficiency(A_f, A_r, eta_f):
    '''
    计算肋片的整体效率

    :param A_f: 肋片的表面积
    :param A_r: 两个肋片之间的根部表面积
    :param eta_f: 肋片的效率
    :return: 肋片的整体效率
    '''
    return (A_r + eta_f * A_f) / (A_r + A_f)
