from CoolProp.CoolProp import PropsSI as psi

# 已知条件：教材 p.223–224，物性按题目给出的平均空气温度。
scale=1/8
u_original,h_model=6.03,195
T_original,T_model=473.15,293.15
nu_o=psi('V','T',T_original,'P',101300,'Air')/psi('D','T',T_original,'P',101300,'Air')
nu_m=psi('V','T',T_model,'P',101300,'Air')/psi('D','T',T_model,'P',101300,'Air')
k_o=psi('L','T',T_original,'P',101300,'Air')
k_m=psi('L','T',T_model,'P',101300,'Air')

# 求解：保持Re、Nu相同，Pr仅近似相同。
u_model=u_original*nu_m/nu_o/scale
h_original=h_model*scale*k_o/k_m

# 输出
print(f'模型流速={u_model:.6f} m/s，实物h={h_original:.6f} W/(m²·K)')
print('Pr存在偏差，是近似模化而非严格相似。')
