import sympy as sp

# 已知条件：教材 p.219，均温颗粒层，单位迎风面积；题目要求符号关系。
y,L,u,rho,cp,h,A=sp.symbols('y L u rho cp h A',positive=True)
t_s,t_in=sp.symbols('t_s t_in',real=True)
t_out=sp.symbols('t_out',real=True)

# 求解：uρcp dt/dy=hA(t_s-t)，入口 t(0)=t_in。
t=t_s-(t_s-t_in)*sp.exp(-h*A*y/(u*rho*cp))
h_solution=u*rho*cp/(A*L)*sp.log((t_s-t_in)/(t_s-t_out))

# 输出
print('流体温度：',t)
print('平均传热系数：',h_solution)
print('Nu/(Re·Pr) = ln[(t_s-t_in)/(t_s-t_out)]/(A·L)，要求 t_in<t_out<t_s。')
print('微分方程残差：',sp.simplify(u*rho*cp*sp.diff(t,y)-h*A*(t_s-t)))
