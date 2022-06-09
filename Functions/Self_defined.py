import numpy as np
import os
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = 'Arial Unicode MS'
plt.rcParams['axes.unicode_minus'] = False


def save_pdf(plt):
    name = os.path.basename(__file__).split(".")[0]
    plt.savefig(f'./{name}.pdf')
    plt.show()


def check_Fo(Fo):
    if (np.array([Fo]) <= 0).any():
        print('Fo数不能小于0，请检查！')
        return None
    if (np.array([Fo]) <= 0.2).any():
        print('Fo数不满足上述公式的要求，上述结果不可靠！')


def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx


if __name__ == '__main__':
    check_Fo(0.1)
    check_Fo([-0.3, 0.4])

