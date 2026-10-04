# 已知条件：教材p.245–246，4排顺排管束，速度为最窄截面速度。
d,u,nu,k,Pr,Pr_wall,rows_factor=.06,8,93.61e-6,.0742,.62,.686,.90

# 求解：对应表6-6顺排管束Re范围，表6-8给出4排修正。
Re=u*d/nu
assert 1e3<Re<2e5
Nu=.27*Re**.63*Pr**.36*(Pr/Pr_wall)**.25
h=rows_factor*Nu*k/d

# 输出
print(f'Re={Re:.6f}，未修正Nu={Nu:.6f}，修正后平均h={h:.6f} W/(m²·K)')
