from CoolProp.CoolProp import PropsSI as psi


import numpy as np
from scipy.optimize import brentq

# 已知条件：教材p.277，Tw(x)-Tb(x)=15K；忽略很短的入口段。
m,d,L,t_in,delta_T=.5,.025,15,10,15

# 求解：平均物性迭代的Dittus–Boelter估计。
def balance(t_out):
 T=(t_in+t_out)/2+273.15
 eta=psi('V','T',T,'P',101300,'Water')
 k=psi('L','T',T,'P',101300,'Water')
 Pr=psi('PRANDTL','T',T,'P',101300,'Water')
 cp=psi('C','T',T,'P',101300,'Water')
 Re=4*m/(np.pi*d*eta)
 h=.023*Re**.8*Pr**.4*k/d
 return m*cp*(t_out-t_in)-h*np.pi*d*L*delta_T

t_out=brentq(balance,t_in,90)

# 输出
print(f'出口温度={t_out:.6f} °C，热平衡残差={balance(t_out):.6g} W')
print('常物性充分发展近似下h恒定，壁流温差恒定等价于恒热流，壁温沿轴向升高。')
print('变物性条件下恒壁流温差并不严格等价于恒热流；此处沿用平均物性工程估计。')
