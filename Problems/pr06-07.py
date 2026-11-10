from CoolProp.CoolProp import PropsSI as psi
import math


# 已知条件：教材p.277，液体10 °C，小温差，均为充分发展管内加热。
u,d,T=1.5,.016,283.15

# 求解：采用Gnielinski充分发展式，R134a物性按饱和液体而非常压气体。
for fluid in ['R134a','Water']:
 if fluid=='R134a': state=('Q',0)
 else: state=('P',101300)
 rho=psi('D','T',T,*state,fluid)
 eta=psi('V','T',T,*state,fluid)
 k=psi('L','T',T,*state,fluid)
 Pr=psi('PRANDTL','T',T,*state,fluid)
 Re=rho*u*d/eta
 f=(1.8*math.log10(Re)-1.5)**(-2)
 Nu=(f/8)*(Re-1000)*Pr/(1+12.7*(f/8)**.5*(Pr**(2/3)-1))
 h=Nu*k/d
 print(f'{fluid}：Re={Re:.6f}，Pr={Pr:.6f}，h={h:.6f} W/(m²·K)')
print('假设R134a为有足够压力防止沸腾的单相液体，使用饱和液体物性作近似。')
