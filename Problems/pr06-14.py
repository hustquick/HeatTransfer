from CoolProp.CoolProp import PropsSI as psi


import numpy as np
from scipy.optimize import brentq

# 已知条件：教材p.277，螺旋直径按管中心线直径处理，忽略螺距对长度影响。
d,D,N,u,t_in,t_wall=.012,.15,4,.6,20,80
R=D/2
L=N*np.pi*D
rho_in=psi('D','T',t_in+273.15,'P',101300,'Water')
m=rho_in*u*np.pi*d*d/4
c_r=1+10.3*(d/R)**3

# 求解：迭代流体平均温度，有限长度及壁面Pr修正的Gnielinski式。
def balance(t_out):
 T=(t_in+t_out)/2+273.15
 eta=psi('V','T',T,'P',101300,'Water')
 k=psi('L','T',T,'P',101300,'Water')
 Pr=psi('PRANDTL','T',T,'P',101300,'Water')
 Pr_w=psi('PRANDTL','T',t_wall+273.15,'P',101300,'Water')
 cp=psi('C','T',T,'P',101300,'Water')
 Re=4*m/(np.pi*d*eta)
 f=(1.8*np.log10(Re)-1.5)**(-2)
 Nu=(f/8)*(Re-1000)*Pr/(1+12.7*np.sqrt(f/8)*(Pr**(2/3)-1))
 Nu*= (1+(d/L)**(2/3))*(Pr/Pr_w)**.11*c_r
 h=Nu*k/d
 return t_out-t_wall-(t_in-t_wall)*np.exp(-h*np.pi*d*L/(m*cp))
t_out=brentq(balance,t_in,t_wall)
T=(t_in+t_out)/2+273.15
Re=4*m/(np.pi*d*psi('V','T',T,'P',101300,'Water'))

# 输出
print(f'L={L:.6f} m，螺旋修正={c_r:.6f}，平均物性Re={Re:.6f}，出口温度={t_out:.6f} °C')
print(f'温度方程残差={balance(t_out):.6g} K')
print('入口附近处于转捩附近，螺旋会改变转捩；按教材湍流修正给出工程近似。')
