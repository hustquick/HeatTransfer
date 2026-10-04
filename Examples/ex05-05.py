# 已知条件：教材 p.220–221，ν取教材定性温度表值。
u=0.5
nu_original=23.13e-6
nu_model=15.06e-6
scale=1/5

# 求解：模型、实物Re相同；Pr近似相同，不是严格相似。
u_model=u*nu_model/nu_original/scale

# 输出
print(f'模型流速={u_model:.6f} m/s')
