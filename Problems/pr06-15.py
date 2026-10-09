from CoolProp.CoolProp import PropsSI as psi


import numpy as np
from scipy.optimize import brentq

# 已知条件：教材p.277，固体石蜡假设初始已在熔点，不计显热和热损失。
d,b,L,m,t_in,t_melt,rho_s,latent=.025,.25,3,.15,60,27.4,770,244e3

# 求解：恒壁温近似，平均水物性随未知出口温度迭代。
def balance(t_out):
 T=(t_in+t_out)/2+273.15
 eta=psi('V','T',T,'P',101300,'Water')
 k=psi('L','T',T,'P',101300,'Water')
 Pr=psi('PRANDTL','T',T,'P',101300,'Water')
 cp=psi('C','T',T,'P',101300,'Water')
 Re=4*m/(np.pi*d*eta)
 Pr_w=psi('PRANDTL','T',t_melt+273.15,'P',101300,'Water')
 f=(1.8*np.log10(Re)-1.5)**(-2)
 Nu=(f/8)*(Re-1000)*Pr/(1+12.7*np.sqrt(f/8)*(Pr**(2/3)-1))
 Nu*= (1+(d/L)**(2/3))*(Pr/Pr_w)**.11
 h=Nu*k/d
 return t_out-t_melt-(t_in-t_melt)*np.exp(-h*np.pi*d*L/(m*cp))
t_out=brentq(balance,t_melt,t_in)
cp=psi('C','T',(t_in+t_out)/2+273.15,'P',101300,'Water')
Q=m*cp*(t_in-t_out)
m_s=rho_s*(b*b-np.pi*d*d/4)*L
seconds=m_s*latent/Q

# 输出
print(f'水出口温度={t_out:.6f} °C，传热功率={Q:.6f} W')
print(f'石蜡质量={m_s:.6f} kg，完全熔化时间={seconds:.6f} s（{seconds/60:.6f} min）')
print('忽略管壁厚度，因此以管内径扣除占据体积；熔化期间壁温维持熔点是题设理想化。')
