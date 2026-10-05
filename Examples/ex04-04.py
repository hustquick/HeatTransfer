import numpy as np
import matplotlib.pyplot as plt

# 已知条件：教材 p.167–168，环肋端部绝热。
# H=r2-r1；m=H*sqrt(h/(λδ))；效率不需要再分别指定 h、λ、δ。
ratio_list = [2, 3, 4]
m_list = [0.1, 0.5, 1, 1.5, 2, 2.5]

# 表4-2：按教材式(4-24)、(4-25)计算，r2/r1=2、m=2。
# N为包含肋根和肋端的节点数；端部采用教材的一阶条件Θ_N=Θ_(N-1)。
node_list = [8, 16, 20, 36, 64, 100]
eta_table42 = []
for N in node_list:
    R_nodes = np.linspace(1, 2, N)
    dR = R_nodes[1]-R_nodes[0]
    A_fd = np.zeros((N, N))
    b_fd = np.zeros(N)
    A_fd[0, 0] = 1
    b_fd[0] = 1
    for i in range(1, N-1):
        A_fd[i, i-1] = 1-dR/(2*R_nodes[i])
        A_fd[i, i] = -2-2*2**2*dR**2
        A_fd[i, i+1] = 1+dR/(2*R_nodes[i])
    A_fd[-1, -1] = 1
    A_fd[-1, -2] = -1
    theta_fd = np.linalg.solve(A_fd, b_fd)
    # 节点代表的环形面积：内部边界取相邻节点中点，两端为半控制体。
    bounds = np.r_[R_nodes[0], (R_nodes[:-1]+R_nodes[1:])/2, R_nodes[-1]]
    area_fd = 2*np.pi*np.diff(bounds**2)
    eta_table42.append(np.sum(area_fd*theta_fd)/np.sum(area_fd))

print('表4-2：节点数对肋效率的影响（r2/r1=2，m=2）')
print('N', *[f'{N:10d}' for N in node_list])
print('η', *[f'{eta:10.3f}' for eta in eta_table42])
print('η详细值', *[f'{eta:10.6f}' for eta in eta_table42])
print()

# 求解：径向环形控制体，两大面散热，肋根 Θ=1。
# 本程序采用单元中心热平衡离散，网格数与课本节点数N不同。
n = 100  # 表4-3采用100个控制体。
efficiencies = []
for ratio in ratio_list:
    R_1, R_2 = 1/(ratio-1), ratio/(ratio-1)
    curve = []
    for m in m_list:
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
        curve.append(eta)
    efficiencies.append(curve)
    plt.plot(m_list,curve,'o-',label=f'r2/r1={ratio}')

# 输出：与教材表4-3一致，行是半径比，列是m。
print('\n环肋效率 η（行：r2/r1；列：m）')
print('r2/r1', *[f'{m:10g}' for m in m_list])
for ratio, curve in zip(ratio_list, efficiencies):
    print(f'{ratio:5d}', *[f'{eta:10.6f}' for eta in curve])
plt.xlabel('m = H sqrt(h / (lambda delta))')
plt.ylabel('Annular fin efficiency')
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()
