A_i = 200e-6
t_fi = 700
h_i = 320
A_o = 2840e-6
t_f = 1000
h_o = 1420
t_o = 820
t_i = 790

Q_in = h_i * (t_i - t_fi) * A_i
Q_out = h_o * (t_f - t_o) * A_o
if abs(Q_in - Q_out) < 0.05 * min(Q_in, Q_out):
    print("叶片的导热处于稳态")
else:
    print("叶子的导热处于非稳态")

