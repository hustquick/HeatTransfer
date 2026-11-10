from CoolProp.CoolProp import PropsSI as psi


import numpy as np
from scipy.optimize import brentq

# 已知条件：教材p.277，内壁恒温100 °C、外壁绝热的环形通道。
d,D,m,t_in,t_out,t_wall=.04,.06,.857,30,50,100
T=(t_in+t_out)/2+273.15
eta=psi('V','T',T,'P',101300,'Water')
k=psi('L','T',T,'P',101300,'Water')
Pr=psi('PRANDTL','T',T,'P',101300,'Water')
cp=psi('C','T',T,'P',101300,'Water')

# 求解：教材允许以水力直径作湍流圆管关联式的近似。
# 大温差采用壁面物性修正Gnielinski；壁面Pr取100°C饱和液体值。
A_flow=np.pi*(D*D-d*d)/4
d_h=D-d
Re=m*d_h/(eta*A_flow)
assert Re>1e4
Pr_w=psi('PRANDTL','T',t_wall+273.15,'Q',0,'Water')
f=(1.8*np.log10(Re)-1.5)**(-2)
Nu_base=(f/8)*(Re-1000)*Pr/(1+12.7*np.sqrt(f/8)*(Pr**(2/3)-1))
Nu_base*= (Pr/Pr_w)**.11
Q=m*cp*(t_out-t_in)
dT_lm=(t_out-t_in)/np.log((t_wall-t_in)/(t_wall-t_out))
# 润湿周长用于水力直径；换热面积只有内管外表面。
def balance(L):
 h=Nu_base*(1+(d_h/L)**(2/3))*k/d_h
 return h*np.pi*d*L*dT_lm-Q
L=brentq(balance,.001,100)
h=Nu_base*(1+(d_h/L)**(2/3))*k/d_h
q_out=h*(t_wall-t_out)

# 输出
print(f'Re={Re:.6f}，h={h:.6f} W/(m²·K)，Q={Q:.6f} W')
print(f'套管长度={L:.6f} m，出口局部热流密度={q_out:.6f} W/m²')
print('采用教材当量直径近似；未包含专门的环隙加热壁修正。水需有足够压力保持单相。')
