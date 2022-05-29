from functions import fin_tip_R

L = 8e-3
# t_0 = t_L
h = 100
lambda_ = 200
delta = 1e-3
a = 100e-3
b = 200e-3
c = 14e-3

H = L / 2
perimeter = 2 *(a + delta)
A_c = a * delta
R = fin_tip_R(H, perimeter, A_c, lambda_, h)
print(f'每片肋片的热阻为：{R:.2f} W/K')
