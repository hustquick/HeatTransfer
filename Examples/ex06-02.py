import numpy as np

# 已知条件：教材p.245，暴露圆管段，15%为辐射和端部导热损失。
d,L,P,loss,t_wall,t_air=.012,.1,40.5,.15,125,15

# 求解：只将剩余功率计入对流，面积取管外侧面积。
Q=P*(1-loss)
A=np.pi*d*L
h=Q/(A*(t_wall-t_air))

# 输出
print(f'对流热量={Q:.6f} W，h={h:.6f} W/(m²·K)')
