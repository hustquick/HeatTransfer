T_oo = 303       # 气流平均温度，K
f = 5           # 温度脉动频率，Hz
v = 20          # 气流速度，m/s
d = 0.9e-3      # 球形热结点直径，m
rho = 8332      # 热结点密度，kg/m³
c_p = 188       # 热结点比热容，J/(kg·K)
lambda_ = 51    # 热结点导热系数，W/(m·K)

# 教材给出的 303 K 空气物性；忽略流体与壁面物性差异的修正项。
nu_air = 16.0e-6     # 运动黏度，m²/s
lambda_air = 2.67e-2 # 导热系数，W/(m·K)
Pr = 0.701

Re = v * d / nu_air
Nu = 2 + (0.4 * Re**0.5 + 0.06 * Re**(2 / 3)) * Pr**0.4
h = Nu * lambda_air / d

# 教材以直径计算 Bi；集中参数法通常采用 V/A = d/6。
Bi_d = h * d / lambda_
Bi = h * (d / 6) / lambda_
if Bi >= 0.1:
    raise ValueError("Bi >= 0.1，不能使用集中参数法计算时间常数。")

# 球体 V/A = d/6，时间常数 tau_c = rho*c_p*V/(h*A)。
tau_c = rho * c_p * d / (6 * h)
period = 1 / f

print(f'空气平均温度 T_oo = {T_oo} K')
print(f'Re = {Re:.0f}')
print(f'Nu = {Nu:.3f}')
print(f'h = {h:.2f} W/(m²·K)')
print(f'Bi（以直径为特征长度）= {Bi_d:.5f}')
print(f'Bi（以 V/A 为特征长度）= {Bi:.5f} < 0.1，适用集中参数法')
print(f'时间常数 tau_c = {tau_c:.3f} s')
print(f'温度脉动周期 = {period:.3f} s')
print(f'时间常数/周期 = {tau_c / period:.2f}')
if tau_c >= period:
    print('结论：时间常数大于脉动周期，该热电偶不能准确跟踪气流温度变化。')
else:
    print('时间常数小于脉动周期；是否满足精度要求还需检查动态响应误差。')
