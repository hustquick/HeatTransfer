from functions import cylindrical_wall_R

t_s2 = 25
t_s1 = 150
lambda_ = 15
r_2 = 35e-3
r_3 = 48e-3

R = cylindrical_wall_R(r_2, r_3, lambda_, 1)
q_r = (t_s1 - t_s2) / R
print(f'q_r = {q_r:.2f} W/m')
