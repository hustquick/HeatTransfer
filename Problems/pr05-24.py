from CoolProp.CoolProp import PropsSI as psi

import argparse

# 已知条件：教材 p.224；水温及风洞空气温度未给，要求输入。
parser=argparse.ArgumentParser(description='5-24：补充水温及风洞气温/°C')
parser.add_argument('--t-water',type=float,required=True)
parser.add_argument('--t-air',type=float,required=True)
args=parser.parse_args()
u_original,scale,p_air=16,1/4,6e5
T_water,T_air=args.t_water+273.15,args.t_air+273.15
nu_water=psi('V','T',T_water,'P',101300,'Water')/psi('D','T',T_water,'P',101300,'Water')
nu_air=psi('V','T',T_air,'P',p_air,'Air')/psi('D','T',T_air,'P',p_air,'Air')

# 求解：以Re相同确定最大模型速度。
u_model=u_original*nu_air/nu_water/scale

# 输出
print(f'最大模型风速={u_model:.6f} m/s')
print('仅可模拟相同几何下的黏性阻力；自由表面、空化、可压缩性需另行判断。')
