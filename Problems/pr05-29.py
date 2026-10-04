from CoolProp.CoolProp import PropsSI as psi

import numpy as np
import matplotlib.pyplot as plt

# 已知条件：教材 p.225，板长0.5 m。
L,u,t_f,t_w=0.5,3.5,15,65
fluid='Water'
T=(t_f+t_w)/2+273.15
rho=psi('D','T',T,'P',101300,fluid)
nu=psi('V','T',T,'P',101300,fluid)/rho
Pr=psi('PRANDTL','T',T,'P',101300,fluid)
Re_c=5e5
x_c=Re_c*nu/u
x=np.linspace(1e-7,L,1000)
Re=u*x/nu

# 求解：层流δ=5x/√Re，湍流δ=0.37x/Re^(1/5)。
# 在Pr>0.5时，湍流热边界层按题目给定近似取为流动边界层。
laminar=Re<=Re_c
delta=np.where(laminar,5*x/np.sqrt(Re),.37*x/Re**.2)
delta_t=np.where(laminar,delta/Pr**(1/3),delta)

# 输出：两经验式在转捩处未必连续，不能理解为真实厚度突变。
print(f'x_c={x_c:.6f} m，Pr={Pr:.6f}，板内是否发生转捩={x_c<L}')
plt.plot(x,delta*1000,label='Velocity layer')
plt.plot(x,delta_t*1000,label='Thermal layer')
if x_c<L: plt.axvline(x_c,color='gray',linestyle='--',label='Transition')
plt.xlabel('x / m')
plt.ylabel('Thickness / mm')
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()
