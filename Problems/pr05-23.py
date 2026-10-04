from CoolProp.CoolProp import PropsSI as psi

# 已知条件：教材 p.224，采用标准大气压强随高度关系，实际气温按题面。
z,u,T,Re_c=10000,600/3.6,233.15,5e5
p=101325*(1-.0065*z/288.15)**5.25588
rho=psi('D','T',T,'P',p,'Air')
nu=psi('V','T',T,'P',p,'Air')/rho

# 求解：平板、零压梯度临界位置；实际机翼曲率及压梯度未计入。
x_c=Re_c*nu/u

# 输出
print(f'采用p={p:.6f} Pa，x_c={x_c:.6f} m')
print('600 km/h的可压缩性会影响真实边界层；这是按教材不可压平板模型估算。')
