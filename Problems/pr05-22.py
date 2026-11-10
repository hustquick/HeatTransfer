import numpy as np

# 已知条件：教材 p.224，定性温度、Pr不变。
L_1,L_2=.5,1
u_1,u_2=15,20
h_1,h_2=40,50

# 求解：在同一L下 h∝u^n；改变L时 h∝u^n L^(n-1)。
n=np.log(h_2/h_1)/np.log(u_2/u_1)
h_new=np.array([h_1,h_2])*(L_2/L_1)**(n-1)

# 输出
print(f'n={n:.8f}，新柱体在15、20 m/s时h={h_new} W/(m²·K)')
