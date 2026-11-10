import numpy as np

# 已知条件：教材 p.221，烟气400 °C、模型空气50 °C，同管径。
u_original=np.array([10.,15.])
nu_smoke=60.38e-6
nu_air=17.95e-6

# 求解：保持Re变化范围一致。
u_model=u_original*nu_air/nu_smoke

# 输出
print(f'模型速度范围={u_model[0]:.6f}–{u_model[1]:.6f} m/s')
print('Pr烟气=0.64、Pr空气=0.698，因此只是近似模化。')
