# 已知条件：教材p.260，竖直密闭空气夹层，70 °C物性。
H,delta,t_hot,t_cold=.5,.015,100,40
nu,k,Pr,g,T=20.02e-6,.0296,.694,9.8,343

# 求解：式6-38a，以间隙为Nu、Gr的特征长度。
Gr=g*(t_hot-t_cold)*delta**3/(T*nu**2)
assert 6e3<=Gr<=2e5 and 11<=H/delta<=42
Nu=.197*(Gr*Pr)**.25*(H/delta)**(-1/9)
h=Nu*k/delta
Q=h*H**2*(t_hot-t_cold)

# 输出
print(f'Gr={Gr:.6f}，Nu={Nu:.6f}，h={h:.6f} W/(m²·K)，Q={Q:.6f} W')
print('这里的Q为气体导热与自然对流合计，不含两壁辐射。')
