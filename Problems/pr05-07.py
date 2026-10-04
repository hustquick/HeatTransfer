from CoolProp.CoolProp import PropsSI as psi

# 已知条件：教材 p.222；梯度40 °C/mm为幅值，坐标从热壁指向空气。
t_w,t_f=80,20
gradient=-40e3
T=(t_w+t_f)/2+273.15
lambda_=psi('L','T',T,'P',101300,'Air')

# 求解：壁面处能量通过分子导热穿过流体界面。
q=-lambda_*gradient

# 输出
print(f'定性温度={T-273.15:g} °C，λ={lambda_:.6g} W/(m·K)，热流密度={q:.6f} W/m²')
