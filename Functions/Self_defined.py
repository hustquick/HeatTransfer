import numpy as np
import os
import matplotlib.pyplot as plt

def save_pdf(name, plt):
    """
    保存pdf文件
    """
    plt.savefig(f'./{name}.pdf')
    plt.show()


def check_Fo(*Fo):
    """
    检查Fo是否符合要求，如果不符合要求，则打印出对应的不符合要求的Fo数的值，并给出提示信息

    :param Fo: Fo的值，可以是一个或多个；如果是容器，在调用时需要加上*，实现解包
    :return:
    """
    for i, Fo_v in enumerate(Fo):
        try:
            assert Fo_v > 0.2
        except AssertionError:
            print(f'第{i+1}个Fo数为{Fo_v:.2f}，不满足Fo数大于0.2的公式使用条件，上述结果不可靠！')


def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx


if __name__ == '__main__':
    check_Fo(0.1)
    check_Fo(-0.3, 0.4, 0.1, 0.6)
    map(check_Fo, [0.5, 0.1, 0.2, 0.2, 0.53, 0.01])  # 对于容器，需要使用map函数对容器中的每个元素调用check_Fo函数
    map(check_Fo, (0.1, 0.2, 0.3, 0.4, 0.5, 0.6))

