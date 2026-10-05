import numpy as np

# 已知条件：Bi=0.1、1、10，求tan(μ)=Bi/μ的前六个正根。
Bi_list = [0.1, 1, 10]
eps = 1e-10

# 求解：逐次迭代，第n个根位于((n−1)π,(n−1/2)π)。
# 在该分支上，μ=(n−1)π+arctan(Bi/μ)。
roots = []
print('Bi      根序号     迭代次数           μ       回代残差')
for Bi in Bi_list:
    row = []
    for n in range(1,7):
        mu = (n-1)*np.pi+np.pi/4  # 区间中点初值。
        for iteration in range(1,10001):
            mu_new = (n-1)*np.pi+np.arctan(Bi/mu)
            error = abs(mu_new-mu)
            mu = mu_new
            if error < eps:
                break
        else:
            raise RuntimeError('迭代未收敛')
        residual = abs(np.tan(mu)-Bi/mu)
        row.append(mu)
        print(f'{Bi:4g} {n:9d} {iteration:12d} {mu:12.8f} {residual:12.2e}')
    roots.append(row)

# 输出：行是Bi，列是根序号。
print('\nBi', *[f'μ{n:>11d}' for n in range(1,7)])
for Bi,row in zip(Bi_list,roots):
    print(f'{Bi:2g}', *[f'{mu:12.8f}' for mu in row])
