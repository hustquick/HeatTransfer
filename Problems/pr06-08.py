from CoolProp.CoolProp import PropsSI as psi


import numpy as np
from scipy.optimize import brentq

# 已知条件：教材p.277，入口体积流量转换为质量流量，管壁平均180 °C。
p,d,qv,t_in,t_out,t_wall=101300,.076,.022,65,115,180
m=psi('D','T',t_in+273.15,'P',p,'Air')*qv
T=(t_in+t_out)/2+273.15
eta=psi('V','T',T,'P',p,'Air')
k=psi('L','T',T,'P',p,'Air')
Pr=psi('PRANDTL','T',T,'P',p,'Air')
cp=psi('C','T',T,'P',p,'Air')
Re=4*m/(np.pi*d*eta)
f=(1.8*np.log10(Re)-1.5)**(-2)
Nu_base=(f/8)*(Re-1000)*Pr/(1+12.7*np.sqrt(f/8)*(Pr**(2/3)-1))
Nu_base*= (T/(t_wall+273.15))**.45
Q=m*cp*(t_out-t_in)
dT_lm=(t_out-t_in)/np.log((t_wall-t_in)/(t_wall-t_out))

# 求解：Gnielinski有限长度修正，气体温差修正按教材式6-9b。
def balance(L):
 h=Nu_base*(1+(d/L)**(2/3))*k/d
 return h*np.pi*d*L*dT_lm-Q
L=brentq(balance,.001,100)

# 输出
print(f'Re={Re:.6f}，质量流量={m:.8f} kg/s，Q={Q:.6f} W，L={L:.6f} m')
print(f'L/d={L/d:.6f}，热平衡残差={balance(L):.6g} W')
