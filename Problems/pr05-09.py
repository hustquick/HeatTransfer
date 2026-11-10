from CoolProp.CoolProp import PropsSI as psi

import numpy as np

# 已知条件：教材 p.223。
T,u=293.15,2
x=np.array([0.1,0.2])
rho=psi('D','T',T,'P',101300,'Water')
nu=psi('V','T',T,'P',101300,'Water')/rho

# 求解：层流平板边界层。
Re=u*x/nu
delta=5*x/np.sqrt(Re)

# 输出
print('x/m、Re、δ/mm：')
print(np.column_stack((x,Re,delta*1000)))
