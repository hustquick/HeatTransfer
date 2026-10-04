import numpy as np

# 已知条件：教材p.277，14号油40 °C物性取附录11 p.548。
d,L,m,t_bulk,t_wall=.0221,1.5,800/3600,40,80
rho,nu,k,Pr,eta_wall=880.7,124.2e-6,.1462,1522,28.4e-4
eta=rho*nu

# 求解：高Pr层流入口区用Sieder–Tate平均关联式。
Re=4*m/(np.pi*d*eta)
assert Re<2300
Nu=1.86*(Re*Pr*d/L)**(1/3)*(eta/eta_wall)**.14
h=Nu*k/d
Q=h*np.pi*d*L*(t_wall-t_bulk)

# 输出
print(f'Re={Re:.6f}，Nu={Nu:.6f}，h={h:.6f} W/(m²·K)，Q={Q:.6f} W')
print('80°C黏度按题面28.4×10^-4 Pa·s；该值与附录14号油表值不同，需审核。')
