import numpy as np

# 已知条件：教材 p.163，半厚度 0.03 m，4 个节点。
delta = 0.06 / 2
dx = 0.01
lambda_ = 40
h = 1000
t_0 = 100
t_f = 0
Fo = 1  # 教材故意采用不稳定的时间步长，以展示数值失稳。
Bi = h * dx / lambda_
t = np.full((8, 4), float(t_0))

# 求解：只用上一时层数据；中心对称，表面对流。
# 教材式(c)应为虚拟节点 t_0^(i)=t_2^(i)，因此中心节点使用二倍差分。
# 数组索引0表示初始时刻；输出按教材表格编号为时层1。
# 式(b)写上标0属于从0起的约定，与表格从1起的编号不一致。
for i in range(7):
    t[i+1, 0] = t[i, 0] + 2*Fo*(t[i, 1] - t[i, 0])
    t[i+1, 1:3] = t[i, 1:3] + Fo*(t[i, :2] - 2*t[i, 1:3] + t[i, 2:])
    t[i+1, 3] = t[i, 3] + 2*Fo*(t[i, 2] - t[i, 3] + Bi*(t_f - t[i, 3]))

# 输出：失稳结果仅用于理解稳定性，不是物理温度预测。
print(f'Bi_Δ = {Bi:.2f}，稳定性要求 Fo_Δ ≤ {1/(2*(1+Bi)):.2f}')
print('行：中心至表面节点 n=1~4；列：时层 i=1~8；温度 / °C')
print('节点 n / 时层 i', *[f'{i:12d}' for i in range(1, 9)])
for n, temperatures in enumerate(t.T, start=1):
    print(f'{n:15d}', *[f'{value:12.2f}' for value in temperatures])
