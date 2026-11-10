from CoolProp.CoolProp import PropsSI as psi

# 已知条件：教材 p.223，实测局部h=149，不用关联式替代测量值。
t_f,t_w,u,x,h=160,30,4,2,149
T=(t_f+t_w)/2+273.15
rho=psi('D','T',T,'P',101300,'Air')
cp=psi('C','T',T,'P',101300,'Air')
nu=psi('V','T',T,'P',101300,'Air')/rho
lambda_=psi('L','T',T,'P',101300,'Air')
Pr=psi('PRANDTL','T',T,'P',101300,'Air')

# 求解：由实测h确定St，再用Colburn比拟估算cf。
Re=u*x/nu
Nu=h*x/lambda_
St=h/(rho*cp*u)
j=St*Pr**(2/3)
cf=2*j

# 输出
print(f'Re_x={Re:.6f}，Nu_x={Nu:.6f}，St={St:.8f}，j={j:.8f}，cf={cf:.8f}')
print('cf由比拟估算；不应把实测h强行调整为光滑平板理论值。')
