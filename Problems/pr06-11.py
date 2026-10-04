# 已知条件：教材p.277，100MW按发电机输出功率处理。
P_out,eff,t_in,t_out,cp,eta,Re=100e6,.985,27,88,14240,.087e-4,1e5

# 求解：发电机损失由氢气带走；正方形边长s的水力直径为s。
Q=P_out*(1/eff-1)
m=Q/(cp*(t_out-t_in))
s=4*m/(eta*Re)
A=s*s

# 输出
print(f'损失功率={Q:.6f} W，氢气流量={m:.6f} kg/s，边长={s:.6f} m，面积={A:.6f} m²')
print('若100MW指输入功率，损失应改为P_in(1-eff)，结果相应不同。')
