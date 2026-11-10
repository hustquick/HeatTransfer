import numpy as np

# 已知条件：教材 p.224；Nu=C Re^n Pr^(1/3)，同一迎风方向。
Re=np.array([5000,20000,41000,90000])
Pr=np.array([2.2,3.9,.7,.7])
Nu=np.array([41,125,117,202])

# 求解：对数线性最小二乘，不把四组不完全一致的数据强行两点拟合。
X=np.column_stack((np.ones(4),np.log(Re)))
log_C,n=np.linalg.lstsq(X,np.log(Nu)-np.log(Pr)/3,rcond=None)[0]
C=np.exp(log_C)
fit=C*Re**n*Pr**(1/3)

# 输出
print(f'C={C:.8f}，n={n:.8f}')
print('Nu实测、拟合、相对残差：')
print(np.column_stack((Nu,fit,(fit-Nu)/Nu)))
print('改变迎风方向会改变分离和尾流结构，不能直接沿用该关联式。')
