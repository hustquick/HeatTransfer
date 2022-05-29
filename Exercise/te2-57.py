import numpy as np
from functions import fin_tip_efficiency2

Diameter = 60e-3
Height = 170e-3
lambda_ = 180
number = 10
delta = 3e-3
H = 25e-3
h = 50
t_f = 28
t_w = 220

Phi_0 = h * np.pi * Diameter * Height * (t_w - t_f)
H_p = H + delta/2
A_L = H_p * delta
efficiency = fin_tip_efficiency2(H_p, A_L, lambda_, h)
fin_tip_area = 2 * np.pi * ((Diameter/2 + H)**2 - (Diameter/2)**2)
Phi_tip = number * efficiency * h * 2 * fin_tip_area *(t_w - t_f)
Phi_base = h * np.pi * Diameter * (Height - number * delta) * (t_w - t_f)
Phi_1 = Phi_tip + Phi_base
times = Phi_1/ Phi_0
print(f'增加了肋片后汽缸散热量是原来的{times:.2f}倍')
