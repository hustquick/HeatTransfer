from CoolProp.CoolProp import PropsSI as psi


# 已知条件：教材p.276–277，恒热流、换热充分发展。
T,p,u,d=373.15,120000,1.5,.025
rho=psi('D','T',T,'P',p,'Air')
eta=psi('V','T',T,'P',p,'Air')
k=psi('L','T',T,'P',p,'Air')

# 求解：先判断流态，层流圆管恒热流Nu=4.36。
Re=rho*u*d/eta
assert Re<2300
h=4.36*k/d

# 输出
print(f'Re={Re:.6f}，h={h:.6f} W/(m²·K)')
