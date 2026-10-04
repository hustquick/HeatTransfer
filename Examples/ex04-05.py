import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve
import matplotlib.pyplot as plt

# 已知条件：教材 p.169–170；计算半厚度 δ 的区域，底边对称。
# 按题目、图4-14和表4-4，采用二维稳态导热、肋端对流。
# 原文假设栏“一维稳态导热”和“顶端绝热”与本例二维计算及其边界条件矛盾。
# 表4-4勘误：3b的系数2属于左邻点；4b左端为Θ[M,1]、分母2+Bi_Δ。
# 下述控制体热平衡自动给出正确系数，推导见ex04-05.md。
conditions = [(50,100,0.02,0.04), (400,8,0.02,0.08)]

# 求解：Θ=(t-t_f)/(t_0-t_f)，肋根 Θ=1，其他外边界对流。
summary = []
fig, axes = plt.subplots(1, 2, figsize=(11, 4))
for case, (h,lambda_,delta,H) in enumerate(conditions, start=1):
    for refine in [1,2,4]:
        nx = round(H/0.005)*refine+1
        # 半厚度网格由同一 Δx=Δy 计算，保留教材 9×5 和 17×5 网格。
        dx = 0.005/refine
        ny = round(delta/dx)+1
        ids = np.arange(nx*ny).reshape(ny,nx)
        A = lil_matrix((nx*ny,nx*ny))
        b = np.zeros(nx*ny)
        for j in range(ny):
            for i in range(nx):
                p = ids[j,i]
                if i==0:
                    A[p,p]=1
                    b[p]=1
                    continue
                # 边界节点控制体是半单元，角点是四分之一单元。
                width = dx*(0.5 if i==nx-1 else 1)
                height = dx*(0.5 if j in [0,ny-1] else 1)
                for dj,di in [(0,-1),(0,1),(-1,0),(1,0)]:
                    jj,ii=j+dj,i+di
                    if not (0<=jj<ny and 0<=ii<nx):
                        if ii==nx or jj==ny:
                            A[p,p] += h*(height if di else width)
                        continue
                    G=lambda_*(height if di else width)/dx
                    A[p,p]+=G
                    A[p,ids[jj,ii]]-=G
        theta=spsolve(A.tocsr(),b).reshape(ny,nx)
        w_x=np.r_[0.5,np.ones(nx-2),0.5]
        w_y=np.r_[0.5,np.ones(ny-2),0.5]
        q_half=h*dx*(np.dot(w_x,theta[-1])+np.dot(w_y,theta[:,-1]))
        eta=q_half/(h*(H+delta))
        print(f'h={h:g}，λ={lambda_:g}，网格 {nx}×{ny}，η二维={eta:.6f}')
    # 一维解析式保留肋端对流，面积分母与二维计算一致。
    m=np.sqrt(h/(lambda_*delta))
    beta=h/(lambda_*m)
    q_1d=lambda_*delta*m*(np.sinh(m*H)+beta*np.cosh(m*H))/(np.cosh(m*H)+beta*np.sinh(m*H))
    eta_1d=q_1d/(h*(H+delta))

    # 输出
    print(f'一维解析 η={eta_1d:.6f}，二维相对差={(eta_1d-eta)/eta*100:.3f}%')
    print('Θ矩阵：从中心对称面至上表面，从肋根至肋端。')
    print(theta[::refine,::refine])

    Bi = h*delta/lambda_
    summary.append((case, Bi, eta, eta_1d, (eta_1d-eta)/eta*100))
    x = np.linspace(0, H, nx)
    y = np.linspace(0, delta, ny)
    contours = axes[case-1].contour(x, y, theta, levels=8)
    axes[case-1].clabel(contours, fmt='%.2f')
    axes[case-1].set(title=f'Case {case}: Bi = {Bi:g}', xlabel='x / m', ylabel='y / m')

# 输出：与教材表4-5一致，行是工况，列是Bi、二维与一维效率及偏差。
print('\n工况       Bi       η二维       η一维       相对偏差/%')
for case, Bi, eta, eta_1d, deviation in summary:
    print(f'{case:4d} {Bi:9.3f} {eta:11.6f} {eta_1d:11.6f} {deviation:13.3f}')
print('Bi小，厚度方向温差小，更适合一维近似；不能只按肋高/厚度比判断。')
fig.tight_layout()
plt.show()
