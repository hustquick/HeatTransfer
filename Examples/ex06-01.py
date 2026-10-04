import numpy as np

# 已知条件：教材p.238–240；采用教材30 °C水物性及40 °C壁温Pr。
d,L,u,t_in,t_out=0.020,5,2,25.3,34.6
k,nu,Pr,rho,cp,Pr_w=.618,.805e-6,5.42,995.7,4177,4.31

# 求解：先用Dittus–Boelter，再按Gnielinski对照。
# 阻力系数沿用本例列出的1.82 lg(Re)-1.5形式。
Re=u*d/nu
Nu_DB=.023*Re**.8*Pr**.4
f=(1.82*np.log10(Re)-1.5)**(-2)
Nu_G=(f/8)*(Re-1000)*Pr/(1+12.7*np.sqrt(f/8)*(Pr**(2/3)-1))
Nu_G*= (1+(d/L)**(2/3))*(Pr/Pr_w)**.11
A=np.pi*d*L
m=rho*u*np.pi*d*d/4
Q=m*cp*(t_out-t_in)

# 输出：恒壁温由指数温升关系反解，使用对数平均温差。
for label,Nu in [('Dittus–Boelter',Nu_DB),('Gnielinski',Nu_G)]:
 h=Nu*k/d
 r=np.exp(h*A/(m*cp))
 t_wall=(r*t_out-t_in)/(r-1)
 print(f'{label}：Re={Re:.1f}，Nu={Nu:.6f}，h={h:.6f} W/(m²·K)，壁温={t_wall:.6f} °C')
print(f'吸热量={Q:.6f} W；关联式有实验误差，两个结果并不完全相同。')
