from Functions.SteadyStateConduction import fin_tip_efficiency2, overall_fin_surface_efficiency

t_0 = 75
t_oo = 25
h = 20
delta = 2e-3
H = 25e-3
W = 12e-2
L = 18e-2
lambda_ = 180
number = 6

H_p = H + delta/2
eta_fin = fin_tip_efficiency2(H_p, H_p*delta, lambda_, h)
print(f'肋片的效率为: {eta_fin:.2%}')
A_f = number * H_p * delta
A_r = (W - number*delta) * L
eta_overall = overall_fin_surface_efficiency(A_f, A_r, eta_fin)
print(f'肋面的总效率为: {eta_overall:.2%}')
R_overall = 1 / (h * (A_f + A_r) * eta_overall)
# 缺少条件，未知底层厚度，这里取肋片的厚度delta
R_conduction = delta / (lambda_ * W*L)
Phi = (t_0 - t_oo) / (R_overall + R_conduction)
print(f'该热沉能散发的热量为：{Phi:.2f} W')
