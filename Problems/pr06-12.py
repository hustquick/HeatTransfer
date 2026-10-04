from CoolProp.CoolProp import PropsSI as psi


import numpy as np

# 已知条件：教材p.277原页明确印为42.05W，保留题面数值。
d_i,d_o,L,u,t_in,P,loss,k_wall=.028,.031,1.5,1.6,10,42.05,.02,18
T=t_in+273.15
rho=psi('D','T',T,'P',101300,'Water')
eta=psi('V','T',T,'P',101300,'Water')
k=psi('L','T',T,'P',101300,'Water')
Pr=psi('PRANDTL','T',T,'P',101300,'Water')
cp=psi('C','T',T,'P',101300,'Water')

# 求解：净加热功率用于水温升，管壁导热按圆筒热阻。
Q=P*(1-loss)
m=rho*u*np.pi*d_i**2/4
Re=rho*u*d_i/eta
h=.023*Re**.8*Pr**.4*k/d_i
t_out=t_in+Q/(m*cp)
t_bulk_mean=(t_in+t_out)/2
t_wall_inner=t_bulk_mean+Q/(h*np.pi*d_i*L)
t_wall_outer=t_wall_inner+Q*np.log(d_o/d_i)/(2*np.pi*k_wall*L)

# 输出
print(f'Re={Re:.6f}，净加热功率={Q:.6f} W，出口温度={t_out:.8f} °C')
print(f'平均外壁温度={t_wall_outer:.8f} °C')
print('若42.05W为原书排印漏掉k的错误，需要另行确认；不擅自改成42.05kW。')
