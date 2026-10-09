from CoolProp.CoolProp import PropsSI as psi
import math


# 已知条件：教材p.277，两种情形流体平均温度相同，均为45 °C。
u,d,T=1.2,.020,318.15
rho=psi('D','T',T,'P',101300,'Water')
eta=psi('V','T',T,'P',101300,'Water')
k=psi('L','T',T,'P',101300,'Water')
Pr=psi('PRANDTL','T',T,'P',101300,'Water')
Re=rho*u*d/eta

# 求解：先输出简单DB估计，再用壁面物性修正的Gnielinski对照。
f=(1.8*math.log10(Re)-1.5)**(-2)
Nu_G=(f/8)*(Re-1000)*Pr/(1+12.7*math.sqrt(f/8)*(Pr**(2/3)-1))
for t_wall,n,label in [(75,.4,'加热'),(15,.3,'冷却')]:
 Pr_w=psi('PRANDTL','T',t_wall+273.15,'P',101300,'Water')
 h_DB=.023*Re**.8*Pr**n*k/d
 h_G=Nu_G*(Pr/Pr_w)**.11*k/d
 print(f'{label}：DB h={h_DB:.6f}，壁面修正Gnielinski h={h_G:.6f} W/(m²·K)')

# 输出
print('平均流体物性相同；加热与冷却差别来自温度边界层中的物性变化。')
print('温差达到30K，DB仅供估计；长管取入口长度修正趋近1。')
