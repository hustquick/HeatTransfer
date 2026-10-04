import numpy as np

# 已知条件：教材p.274，充分发展湍流、恒壁温，沿用22.5 °C表值。
d,qv,roughness,t_in,t_out,t_wall=.4,.558,.0025,25,20,18
k,nu,Pr,rho,cp=.0261,15.3e-6,.701,1.195,1005

# 求解：按教材完全粗糙阻力平方区近似，再用Gnielinski式。
u=qv/(np.pi*d*d/4)
Re=u*d/nu
Re_threshold=4160*(.5*d/(2*roughness))**.85
assert Re>Re_threshold
f=(1.74+2*np.log10(d/(2*roughness)))**(-2)
Nu=(f/8)*(Re-1000)*Pr/(1+12.7*np.sqrt(f/8)*(Pr**(2/3)-1))
h=Nu*k/d
Q=rho*qv*cp*(t_in-t_out)
dT_lm=(t_in-t_out)/np.log((t_in-t_wall)/(t_out-t_wall))
L=Q/(h*np.pi*d*dT_lm)

# 输出
print(f'Re={Re:.6f}，f={f:.6f}，Nu={Nu:.6f}，h={h:.6f} W/(m²·K)')
print(f'制冷量={Q:.6f} W，对数平均温差={dT_lm:.6f} K，管长={L:.6f} m')
print('忽略土壤随时间升温、弯头和入口效应；恒定18°C壁温是理想假设。')
