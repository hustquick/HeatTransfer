import numpy as np

# 已知条件：教材p.249，60 °C物性；圆形冲击区半径r。
d,H,r,u,k,nu,Pr=.025,.1,.15,25,.029,18.97e-6,.696

# 求解：式6-23，Nu特征长度为喷嘴直径，不是区域半径。
Re=u*d/nu
assert 2e3<=Re<=4e5 and 2<=H/d<=12 and 2.5<=r/d<=7.5
Nu=2*Re**.5*Pr**.42*(1+.005*Re**.55)**.5
Nu*= (1-1.1*d/r)/(1+.1*(H/d-6)*d/r)*d/r
h=Nu*k/d
Re_plate=u*r/nu
Nu_plate=.664*np.sqrt(Re_plate)*Pr**(1/3)
h_plate=Nu_plate*k/r

# 输出：对照同样长度r的层流平板，不误用喷口距离H。
print(f'射流Re={Re:.6f}，Nu={Nu:.6f}，h={h:.6f} W/(m²·K)')
print(f'平板h={h_plate:.6f} W/(m²·K)，射流/平板={h/h_plate:.6f}')

print('教材代入步骤混用了0.10m与0.05m，平板h又以0.10m作分母；本脚本统一使用题给r=0.15m。')
