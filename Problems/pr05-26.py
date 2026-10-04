from CoolProp.CoolProp import PropsSI as psi

# 已知条件：教材 p.223–224，测得的是总切向力，而不是切应力/Pa。
u,F,t_f,t_w=1.2,0.14,30,200
T=(t_f+t_w)/2+273.15
cp=psi('C','T',T,'P',101300,'Air')
Pr=psi('PRANDTL','T',T,'P',101300,'Air')

# 求解：积分Colburn比拟，Q=F cp (t_w-t_f)/(u Pr^(2/3))。
Q=F*cp/u*Pr**(-2/3)*(t_w-t_f)

# 输出：正值从物体散出，负值是进入物体的热负荷。
print(f'与测得总切向力对应的对流热量={Q:.6f} W')
print(f'若两侧同时暴露于相同气流，总散热量={2*Q:.6f} W；题面F只对应一侧。')
