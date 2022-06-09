import scipy.constants as sc

Phi_1 = 400
Phi_2 = 800
C = 5e5
tau = 1 * sc.hour

Phi = Phi_2 - Phi_1
Delta_T = Phi / C * tau
print(f"该男子的平均体温下降{Delta_T:.2f}度")
