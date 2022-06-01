import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = 'Arial Unicode MS'
plt.rcParams['axes.unicode_minus'] = False

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
for i, h in enumerate(h_out):
    print(f' 当传热系数为{h} W/m^2-K 时，散热量为{Q[i]:.2f} W')
fig, ax = plt.subplots()
ax.plot(h_out, Q, 'o-')
ax.set_xlabel('传热系数(W/m^2-K)')
ax.set_ylabel('散热量(W)')
ax.set_title('散热量与传热系数的关系')
plt.savefig('te1-41.pdf')
plt.show()