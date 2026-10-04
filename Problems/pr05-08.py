from CoolProp.CoolProp import PropsSI as psi

# 已知条件：教材 p.222–223；14号润滑油采用附录11（p.548）。
# 25 °C介于20和30 °C之间，这里对运动黏度作线性插值。
nu_oil=(410.9+216.5)/2*1e-6
Re_c,u,T=5e5,1,298.15

# 求解：x_c=Re_c ν/u；油不能用另一种油的物性静默替代。
for fluid in ['Air','Water']:
 rho=psi('D','T',T,'P',101300,fluid)
 eta=psi('V','T',T,'P',101300,fluid)
 print(f'{fluid}：x_c={Re_c*eta/rho/u:.6f} m')

# 输出
print(f'14号润滑油：ν={nu_oil:.7f} m²/s，x_c={Re_c*nu_oil/u:.6f} m')
print('油黏度随温度变化很强；结果对应表值线性插值。')
