import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve
import matplotlib.pyplot as plt

# 已知条件：计算半厚度δ区域，肋根定温，底部对称绝热。
# 上表面及肋端对流；h、λ、δ、H分别为换热系数、导热系数、半厚度、肋高。
conditions = [(50,100,0.02,0.04), (400,8,0.02,0.08)]

# 求解：Θ=(t-t_f)/(t_0-t_f)，肋根 Θ=1，其他外边界对流。
summary = []
fig, axes = plt.subplots(1, 2, figsize=(11, 4))
for case, (h,lambda_,delta,H) in enumerate(conditions, start=1):
    dx = 0.005  # Δx=Δy
    nx = round(H/dx)+1
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
    # 一维计算：修正肋高的一维近似，H_c=H+δ。
    m=np.sqrt(h/(lambda_*delta))
    eta_1d=np.tanh(m*(H+delta))/(m*(H+delta))

    Bi = h*delta/lambda_
    summary.append((case, nx, ny, Bi, eta, eta_1d, abs(eta_1d-eta)/eta*100))
    x = np.linspace(0, H, nx)
    y = np.linspace(0, delta, ny)
    contours = axes[case-1].contour(x, y, theta, levels=8)
    axes[case-1].clabel(contours, fmt='%.2f')
    axes[case-1].set(title=f'Case {case}: Bi = {Bi:g}', xlabel='x / m', ylabel='y / m')

# 输出：各列均由上述计算得到，相对偏差以二维效率为基准。
print('工况   节点M×N       Bi       η二维       η一维       相对偏差/%')
for case, nx, ny, Bi, eta, eta_1d, deviation in summary:
    grid = f'{nx}×{ny}'
    print(f'{case:4d} {grid:>9s} {Bi:9.3f} {eta:11.6f} {eta_1d:11.6f} {deviation:13.3f}')
fig.tight_layout()
plt.show()
