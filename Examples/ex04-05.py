import numpy as np
import matplotlib.pyplot as plt

# 教材假设栏勘误：本例为二维稳态导热；应为肋片底端（y=0对称面）绝热，
# 不是顶端（x=H肋端）绝热；顶端与上表面均对流换热。
# 教材表4-4勘误：m沿肋根至肋端，n沿对称面至上表面；Bi_Δ=hΔ/λ。
# 3b（m=M，n=2…N−1）：
# Θ[M,n]=(2Θ[M−1,n]+Θ[M,n+1]+Θ[M,n−1])/(4+2Bi_Δ)。
# 左邻点系数应为2；控制体左侧导热系数为λ，上下各为λ/2。
# 4b（右下角）：左端应为Θ[M,1]，不是Θ[M,N]；
# Θ[M,1]=(Θ[M−1,1]+Θ[M,2])/(2+Bi_Δ)，不是分母2+2Bi_Δ。
# 此角点底部绝热，仅右侧对流；两个导热系数为λ/2，对流系数为hΔ/2。
# 分母2+2Bi_Δ适用于有两个对流面的右上角4a。

# 已知条件：h、λ、半厚度δ、肋高H；肋根Θ=1。
# 底部对称绝热，上表面与肋端对流；Δx=Δy。
conditions = [(50,100,0.02,0.04), (400,8,0.02,0.08)]
dx = 0.005
eps = 1e-9
summary = []
fig, axes = plt.subplots(1,2,figsize=(11,4))

# 求解：Gauss-Seidel，每次更新后立即使用新值。
for case,(h,lambda_,delta,H) in enumerate(conditions,start=1):
    M,N = round(H/dx)+1,round(delta/dx)+1
    Bi_grid = h*dx/lambda_
    theta = np.ones((N,M))
    for iteration in range(1,100001):
        old = theta.copy()
        # 底部绝热（1）与内部节点（2）。
        for m in range(1,M-1):
            theta[0,m] = (theta[0,m-1]+theta[0,m+1]+2*theta[1,m])/4
        for n in range(1,N-1):
            for m in range(1,M-1):
                theta[n,m] = (theta[n-1,m]+theta[n+1,m]+theta[n,m-1]+theta[n,m+1])/4
        # 上表面对流（3a）与肋端对流（3b）。
        for m in range(1,M-1):
            theta[-1,m] = (theta[-1,m-1]+theta[-1,m+1]+2*theta[-2,m])/(4+2*Bi_grid)
        for n in range(1,N-1):
            theta[n,-1] = (theta[n-1,-1]+theta[n+1,-1]+2*theta[n,-2])/(4+2*Bi_grid)
        # 右上角两个对流面（4a），右下角一个对流面（4b）。
        theta[-1,-1] = (theta[-1,-2]+theta[-2,-1])/(2+2*Bi_grid)
        theta[0,-1] = (theta[0,-2]+theta[1,-1])/(2+Bi_grid)
        if np.max(np.abs(theta-old)) < eps:
            break
    else:
        raise RuntimeError('迭代未收敛')

    # 散热边界梯形积分，右上角计入两个半段。
    total = 0.5*(theta[-1,0]+theta[0,-1])
    total += np.sum(theta[-1,1:])+np.sum(theta[1:-1,-1])
    eta = total/(M+N-2)
    m_fin = np.sqrt(h/(lambda_*delta))
    eta_1d = np.tanh(m_fin*(H+delta))/(m_fin*(H+delta))
    Bi = h*delta/lambda_
    deviation = abs(eta_1d-eta)/eta*100
    summary.append((case,M,N,Bi,eta,eta_1d,deviation))
    print(f'工况{case}：迭代{iteration}次')
    contours = axes[case-1].contour(np.linspace(0,H,M),np.linspace(0,delta,N),theta,levels=8)
    axes[case-1].clabel(contours,fmt='%.2f')
    axes[case-1].set(title=f'Case {case}: Bi={Bi:g}',xlabel='x / m',ylabel='y / m')

# 输出：表4-5的各列均为计算结果；图4-16为两工况等温线。
print('工况   节点M×N       Bi       η二维       η一维       相对偏差/%')
for case,M,N,Bi,eta,eta_1d,deviation in summary:
    grid = f'{M}×{N}'
    print(f'{case:4d} {grid:>9s} {Bi:9.3f} {eta:11.6f} {eta_1d:11.6f} {deviation:13.3f}')
fig.tight_layout()
plt.show()
