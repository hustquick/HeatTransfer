import numpy as np

# 已知条件：教材p.273，忽略辐射及端部导热，30 °C空气物性。
d,L,I,R,t_wall,t_air=20e-6,2e-3,.150,.4164,40,20
k,nu,Pr=.0267,16e-6,.701

# 求解：Hilpert分段关联式反解Re，并检验所属范围。
Q=I**2*R
h=Q/(np.pi*d*L*(t_wall-t_air))
Nu=h*d/k
ranges=[(.4,4,.989,.330),(4,40,.911,.385),(40,4000,.683,.466),(4000,40000,.193,.618),(40000,400000,.027,.805)]
for lo,hi,C,n in ranges:
 Re=(Nu/(C*Pr**(1/3)))**(1/n)
 if lo<=Re<=hi:
  u=Re*nu/d
  print(f'有效Re范围={lo}–{hi}，Re={Re:.6f}，速度={u:.6f} m/s')
  break
else: raise ValueError('没有符合关联式范围的解')

# 输出
print(f'电功率={Q:.8f} W，h={h:.6f} W/(m²·K)，Nu={Nu:.6f}')
