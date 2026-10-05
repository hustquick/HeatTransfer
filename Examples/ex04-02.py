# 例题 4-2：二维稳态导热问题的数值解，Gauss-Seidel迭代法

# 边界温度（上边界500°C，其余边界100°C）
T_top = 500
T_left = 100
T_right = 100
T_bottom = 100

# 初始内部节点温度（上排300°C，下排200°C）
T1 = 300.0
T2 = 300.0
T3 = 200.0
T4 = 200.0

# 收敛阈值与最大迭代次数
eps = 2e-4
max_iter = 100

print(f"{'迭代次数':<6} {'T1':>10} {'T2':>10} {'T3':>10} {'T4':>10}")
print(f"{0:<6} {T1:10.2f} {T2:10.2f} {T3:10.2f} {T4:10.2f}")

for k in range(1, max_iter + 1):
    T1_new = 0.25 * (T_left + T_top + T2 + T3)
    T2_new = 0.25 * (T1_new + T_top + T4 + T_right)
    T3_new = 0.25 * (T_left + T1_new + T4 + T_bottom)
    T4_new = 0.25 * (T2_new + T3_new + T_bottom + T_right)

    print(f"{k:<6} {T1_new:10.2f} {T2_new:10.2f} {T3_new:10.2f} {T4_new:10.2f}")

    # 相对变化判据；先保存本次结果，再判断是否停止。
    error = max(abs((T1_new-T1)/T1_new), abs((T2_new-T2)/T2_new),
                abs((T3_new-T3)/T3_new), abs((T4_new-T4)/T4_new))
    T1, T2, T3, T4 = T1_new, T2_new, T3_new, T4_new
    if error < eps:
        break
else:
    raise RuntimeError('迭代未收敛')

# 输出：图4-7的网格、边界条件和计算节点。
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
for position in range(4):
    ax.plot([position,position],[0,3],color='gray')
    ax.plot([0,3],[position,position],color='gray')
for x,y,index,value in [(1,2,1,T1),(2,2,2,T2),(1,1,3,T3),(2,1,4,T4)]:
    ax.plot(x,y,'ko')
    ax.text(x+0.08,y+0.08,f'{index}: {value:.2f} C')
for x,y,value in [(1.5,3.2,T_top),(-0.3,1.5,T_left),(3.3,1.5,T_right),(1.5,-0.2,T_bottom)]:
    ax.text(x,y,f'{value} C',ha='center',va='center')
ax.set_aspect('equal')
ax.set(xlim=(-0.7,3.7),ylim=(-0.5,3.5),title='Example 4-2: grid and temperatures')
ax.axis('off')
fig.tight_layout()
plt.show()
