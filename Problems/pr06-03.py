import numpy as np

# 已知条件：教材p.276，变压器油运动黏度为3.8×10^-5 m²/s。
d,L,m,rho,nu,Pr=.03,2,.313,885,3.8e-5,490

# 求解：层流入口长度的数量级估计。
u=m/(rho*np.pi*d*d/4)
Re=u*d/nu
L_h=.05*Re*d
L_t=.05*Re*Pr*d

# 输出
print(f'u={u:.6f} m/s，Re={Re:.6f}，水动力入口长度≈{L_h:.6f} m，热入口长度≈{L_t:.6f} m')
print('为层流；2m末端速度分布近于充分发展，温度分布仍在发展。')
