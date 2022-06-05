from Functions.SteadyStateConduction import cylinder_Delta_T_with_heat_source

r = 2e-2
Phi_dot = 5650
t_o = 37
lambda_ = 0.42

Delta_T = cylinder_Delta_T_with_heat_source(r, lambda_, Phi_dot)
print(f'由于肌肉运动所造成的最大温升为{Delta_T:.2f} C')
