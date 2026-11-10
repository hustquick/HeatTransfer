import numpy as np

# 已知条件：教材 p.203，物性取定性温度30 °C，保留教材表值。
u=10
nu=16e-6
Pr=0.701
x=np.array([50,100,150,200,250,300,320])*1e-3

# 求解：层流平板边界层，Re_x<5×10^5。
Re=u*x/nu
delta=5*x/np.sqrt(Re)
delta_t=delta/Pr**(1/3)

# 输出
print('x/m、Re_x、δ/mm、δ_t/mm：')
print(np.column_stack((x,Re,delta*1000,delta_t*1000)))
