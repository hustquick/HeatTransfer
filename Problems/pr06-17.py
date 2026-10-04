import numpy as np

# 已知条件：教材p.277–278，甘油27 °C物性，流体允许温升6K。
D,H,d,Q,t_in,t_out,t_wall=.3,.5,.02,1000,24,30,47
rho,cp,k,eta,Pr,eta_wall=1259.9,2427,.286,.799,6780,.2095

# 求解：极低Re，高Pr热入口区；用Sieder–Tate而不套湍流螺旋修正。
m=Q/(cp*(t_out-t_in))
Re=4*m/(np.pi*d*eta)
dT_lm=(t_out-t_in)/np.log((t_wall-t_in)/(t_wall-t_out))
B=1.86*k/d*(Re*Pr*d)**(1/3)*(eta/eta_wall)**.14
# h=B/L^(1/3)，Q=B πd ΔT_lm L^(2/3)。
L=(Q/(B*np.pi*d*dT_lm))**1.5
h=B/L**(1/3)
# 管壁厚度未给，近似中心线直径D+d，忽略端部直管。
D_coil=D+d
N=L/(np.pi*D_coil)
pitch=H/N
Dean=Re*np.sqrt(d/D_coil)

# 输出
print(f'甘油流量={m:.8f} kg/s，Re={Re:.6f}，Dean={Dean:.6f}')
print(f'平均h={h:.6f} W/(m²·K)，总管长={L:.6f} m，近似圈数={N:.6f}，相邻圈中心距={pitch:.6f} m')
assert pitch>d, '按给定高度无法容纳所需圈数'
print('Dean很小，二次流影响弱；中心距是连续缠绕估计，实际整数圈数和管外径需另定。')
