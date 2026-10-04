from CoolProp.CoolProp import PropsSI as psi

import argparse

# 已知条件：教材 p.223；给出壁面切应力，但没有给流速。
parser=argparse.ArgumentParser(description='5-14：需补充水的来流速度/m/s')
parser.add_argument('--velocity',type=float,required=True)
u=parser.parse_args().velocity
if u<=0: raise ValueError('流速必须为正')
t_f,t_w,tau=15,60,1.5
T=(t_f+t_w)/2+273.15
cp=psi('C','T',T,'P',101300,'Water')
Pr=psi('PRANDTL','T',T,'P',101300,'Water')

# 求解：Colburn比拟 St Pr^(2/3)=cf/2。
h=tau*cp/u*Pr**(-2/3)
q=h*(t_w-t_f)

# 输出
print(f'h={h:.6f} W/(m²·K)，q={q:.6f} W/m²')
print('缺少速度时只能给出 q·u；不能由切应力单独求出q。')
