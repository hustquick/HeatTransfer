import numpy as np
from scipy.special import iv, kv
import matplotlib.pyplot as plt

# 已知条件：教材 p.167–168，环肋端部绝热。
# H=r2-r1；m=H*sqrt(h/(λδ))；效率不需要再分别指定 h、λ、δ。
ratio_list = [2, 3, 4]
m_list = [0.1, 0.5, 1, 1.5, 2, 2.5]

# 求解：径向环形控制体，两大面散热，肋根 Θ=1。
# 本程序采用单元中心热平衡离散，网格数与课本节点数N不同。
efficiencies = []
max_error = 0
for ratio in ratio_list:
    R_1, R_2 = 1/(ratio-1), ratio/(ratio-1)
    curve = []
    for m in m_list:
        for n in [20, 40, 80, 160]:
            faces = np.linspace(R_1,R_2,n+1)
            R = (faces[:-1]+faces[1:])/2
            G = 2*np.pi/np.log(R[1:]/R[:-1])
            G_base = 2*np.pi/np.log(R[0]/R_1)
            area = 2*np.pi*np.diff(faces**2)
            A = np.diag(np.r_[G_base,G]+np.r_[G,0]+m**2*area)
            A += np.diag(-G,1)+np.diag(-G,-1)
            b = np.zeros(n)
            b[0] = G_base
            theta = np.linalg.solve(A,b)
            eta = np.sum(area*theta)/np.sum(area)
            if ratio == 2 and m == 2:
                print(f'网格校核：控制体数={n:3d}，η={eta:.6f}')
        # 独立校核：修正贝塞尔函数的解析环肋解。
        k = np.sqrt(2)*m
        coefficients = np.linalg.solve(
            [[iv(0,k*R_1),kv(0,k*R_1)], [iv(1,k*R_2),-kv(1,k*R_2)]], [1,0])
        q_exact = 2*np.pi*R_1*k*(coefficients[1]*kv(1,k*R_1)-coefficients[0]*iv(1,k*R_1))
        eta_exact = q_exact/(2*m**2*np.pi*(R_2**2-R_1**2))
        max_error = max(max_error, abs(eta-eta_exact))
        curve.append(eta)
    efficiencies.append(curve)
    plt.plot(m_list,curve,'o-',label=f'r2/r1={ratio}')

# 输出：与教材表4-3一致，行是半径比，列是m。
print('\n环肋效率 η（行：r2/r1；列：m）')
print('r2/r1', *[f'{m:10g}' for m in m_list])
for ratio, curve in zip(ratio_list, efficiencies):
    print(f'{ratio:5d}', *[f'{eta:10.6f}' for eta in curve])
print(f'与解析解的最大绝对误差：{max_error:.3e}')
plt.xlabel('m = H sqrt(h / (lambda delta))')
plt.ylabel('Annular fin efficiency')
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()
