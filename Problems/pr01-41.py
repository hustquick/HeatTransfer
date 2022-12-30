import numpy as np
import matplotlib.pyplot as plt
import os

import sys
sys.path.append("..")
from Functions.Self_defined import save_pdf

delta = 200e-3
h = 3
w = 6
t_in = 2
t_out = -10
h_in = 6
# ratio_list = [1, 0.5, 0.25]
# h_out_base = 60
h_out = np.array([10, 15, 25, 32, 45, 60])
lambda_ = 0.044

R_1 = 1 / h_in
R_2 = delta / lambda_
R_3 = 1 / h_out
R = R_1 + R_2 + R_3
A = h * w
Q = A * (t_in - t_out) / R
for h, Q_ in zip(h_out, Q):
    print(f'当传热系数为{h} W/m^2-K 时，散热量为{Q_:.2f} W')
fig, ax = plt.subplots()
ax.plot(h_out, Q, 'o-')
ax.set_xlabel('传热系数($\mathrm{W/m^2 \cdot K}$)')
ax.set_ylabel('散热量($\mathrm{W}$)')
ax.set_title('散热量与传热系数的关系')
name = os.path.basename(__file__).split(".")[0]
save_pdf(name, plt)
