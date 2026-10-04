from CoolProp.CoolProp import PropsSI as psi

import numpy as np

# 已知条件：教材 p.223；物性按壁面和流体平均温度。
t_f,t_w,u=20,50,2.5
x=np.array([2.0])
T=(t_f+t_w)/2+273.15
rho=psi('D','T',T,'P',101300,'Air')
nu=psi('V','T',T,'P',101300,'Air')/rho
lambda_=psi('L','T',T,'P',101300,'Air')
Pr=psi('PRANDTL','T',T,'P',101300,'Air')

# 求解：层流平板，局部和从前缘至x的平均系数分开。
Re=u*x/nu
if np.any(Re>=5e5): raise ValueError('超出所用层流范围')
delta=5*x/np.sqrt(Re)
delta_t=delta/Pr**(1/3)
cf=0.664/np.sqrt(Re)
tau=cf*rho*u**2/2
h=0.332*np.sqrt(Re)*Pr**(1/3)*lambda_/x
cf_mean=2*cf
h_mean=2*h

# 输出
print('x/m、Re、δ/mm、δt/mm、τ/Pa、h、平均cf、平均h：')
print(np.column_stack((x,Re,delta*1000,delta_t*1000,tau,h,cf_mean,h_mean)))
