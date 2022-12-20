import numpy as np
from Functions.SteadyStateConduction import fin_tip_efficiency, overall_fin_surface_efficiency
import matplotlib.pyplot as plt
import os
from Functions.Self_defined import save_pdf

d = 7.5e-3
distance = 10e-3
t_f = 25
t_w = 120
W = 10e-2

L = 6e-2  # 圆柱的高度。缺少条件，这里自己取的6 cm。
lambda_ = 180  # 导热系数。缺少条件，这里自己取的180 W/(m-K)。


def h(u):
    return 5.12 * u**0.65 / d**0.35


u = np.array([0.6, 1.0, 1.5, 2.0, 2.5])
h = h(u)

perimeter = np.pi * d
A_c = np.pi * (d/2)**2
H_p = L + A_c / perimeter
eta_fin = fin_tip_efficiency(H_p, perimeter, A_c, lambda_, h)
# print(f'肋片的效率为: {eta_fin:.2%}')
number = 10*10
A_f = number * H_p * perimeter
A_r = W*W - number*A_c
eta_overall = overall_fin_surface_efficiency(A_f, A_r, eta_fin)
# print(f'肋面的总效率为: {eta_overall:.2%}')
R_overall = 1 / (h * (A_f + A_r) * eta_overall)
Phi = (t_w - t_f) / R_overall
[print(f'当空气流速为{speed} m/s时，散热量为：{phi:.2f} W') for (speed, phi) in zip(u, Phi)]

fig, ax = plt.subplots()
ax.plot(u, Phi)
ax.set_xlabel('空气流速（$\mathrm{m/s}$）')
ax.set_ylabel('散热量（$\mathrm{W}$）')
ax.set_title('散热量随空气流速的变化')
name = os.path.basename(__file__).split(".")[0]
save_pdf(name, plt)
