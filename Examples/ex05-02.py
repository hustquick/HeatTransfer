import numpy as np

# 已知条件：教材 p.204，平板单面换热；辐射不计。
L,width=0.32,1
u,nu,Pr,lambda_=10,16e-6,0.701,0.0267
t_w,t_f=40,20

# 求解
Re=u*L/nu
Nu=0.664*np.sqrt(Re)*Pr**(1/3)
h=Nu*lambda_/L
Q=h*L*width*(t_w-t_f)

# 输出
print(f'Re={Re:.0f}，Nu={Nu:.6f}，h={h:.6f} W/(m²·K)，Q={Q:.6f} W')
