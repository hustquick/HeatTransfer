t1 = 0.0
t2 = 0.0
t3 = 0.0

# 收敛阈值和最大迭代次数
eps = 5e-4
max_iter = 100

print(f"{'迭代次数':<3} {'t1':>10} {'t2':>10} {'t3':>10}")
print(f"{0:<8} {t1:10.3f} {t2:10.3f} {t3:10.3f}")

for k in range(1, max_iter + 1):
    t1_new = (29 - 2 * t2 - t3) / 8
    t2_new = (32 - t1_new - 2*t3) / 5
    t3_new = (28 - 2*t1_new - t2_new) / 4

    print(f"{k:<8} {t1_new:10.3f} {t2_new:10.3f} {t3_new:10.3f}")

    error = max(abs(t1_new-t1), abs(t2_new-t2), abs(t3_new-t3))
    t1, t2, t3 = t1_new, t2_new, t3_new
    if error < eps:
        break

else:
    raise RuntimeError('迭代未收敛')

# 输出：代回原方程。
residual = max(abs(8*t1+2*t2+t3-29), abs(t1+5*t2+2*t3-32), abs(2*t1+t2+4*t3-28))
print(f'最大方程残差：{residual:.3e}')
