import numpy as np

# 已知条件：教材p.259–260，水平段15m，竖直段1.5m，60 °C空气物性。
d,L_vertical,L_horizontal,t_wall,t_air=.15,1.5,15,110,10
k,nu,Pr,g,T=.029,18.97e-6,.696,9.8,333

# 求解：竖直段以高度、水平段以直径为特征长度。
Ra_v=g*(t_wall-t_air)*L_vertical**3/(T*nu**2)*Pr
Ra_h=g*(t_wall-t_air)*d**3/(T*nu**2)*Pr
Nu_v=.11*Ra_v**(1/3)
Nu_h=.48*Ra_h**.25
h_v,h_h=Nu_v*k/L_vertical,Nu_h*k/d
Q_v=h_v*np.pi*d*L_vertical*(t_wall-t_air)
Q_h=h_h*np.pi*d*L_horizontal*(t_wall-t_air)

# 输出：题目问每小时热量；同时给出瞬时热功率。
print(f'竖直段Ra={Ra_v:.6g}，h={h_v:.6f}，Q={Q_v:.6f} W')
print(f'水平段Ra={Ra_h:.6g}，h={h_h:.6f}，Q={Q_h:.6f} W')
print(f'总对流功率={Q_v+Q_h:.6f} W，每小时对流散热量={(Q_v+Q_h)*3600/1e6:.6f} MJ')
print('不含辐射；两段交汇影响与端面换热忽略。')
