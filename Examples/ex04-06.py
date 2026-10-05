import numpy as np
import matplotlib.pyplot as plt

# 已知条件：教材 p.170–171，单面受热、另面绝热，原板厚 δ=0.1 m。
delta=0.1
t_0,t_f=80,300
h,lambda_,a=1163,50,1.39e-5
n=10
dx=delta/n
Bi=h*dx/lambda_
x=np.linspace(0,delta,n+1)
fig,axes=plt.subplots(1,2,figsize=(11,5))
times=np.array([36,180,360,540,720,900,1080,1260,1440,1800])

# 求解：11节点显式差分；x=0 绝热，x=δ 对流。
for dt,marker in zip([1.8,0.18,0.018],['^','o','x']):
    Fo=a*dt/dx**2
    if Fo>1/(2*(1+Bi)):
        raise ValueError('时间步长不满足对流边界稳定性条件')
    t=np.full(n+1,float(t_0))
    snapshots=[]
    target_steps=np.rint(times/dt).astype(int)
    for step in range(1,target_steps[-1]+1):
        old=t.copy()
        t[1:-1]=old[1:-1]+Fo*(old[:-2]-2*old[1:-1]+old[2:])
        t[0]=old[0]+2*Fo*(old[1]-old[0])
        t[-1]=old[-1]+2*Fo*(old[-2]-old[-1]+Bi*(t_f-old[-1]))
        if step in target_steps:
            snapshots.append(t.copy())
    snapshots=np.array(snapshots)
    print(f'Δτ={dt:g} s，Fo_Δ={Fo:.6f}，允许 Fo_Δ≤{1/(2*(1+Bi)):.6f}')
    print('列：时刻/s、绝热面温度、受热面温度/°C')
    print(np.column_stack((times,snapshots[:,0],snapshots[:,-1])))
    if dt==0.18:
        print('温度表：行是时刻，列是x=0、0.01、…、0.10 m的节点温度。')
        print(np.column_stack((times,snapshots)).round(3))
        for tau,temp in zip(times,snapshots):
            axes[0].plot(x,temp,'o-',label=f'{tau/60:g} min')
    for tau in [180,900,1800]:
        index=np.where(times==tau)[0][0]
        axes[1].plot(x,snapshots[index],marker=marker,markersize=4,label=f'{tau/60:g} min, dt={dt:g} s')

# 输出：温度分布与时间步长影响；横坐标方向与课本一致。
for ax,title in zip(axes,['Temperature profiles (dt=0.18 s)','Time-step comparison']):
    ax.set(title=title,xlabel='x / m (0: adiabatic, 0.1: heated)',ylabel='Temperature / degC')
    ax.invert_xaxis()
    ax.legend(fontsize=8,ncol=2)
    ax.grid()
fig.tight_layout()
plt.show()
