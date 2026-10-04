# 已知条件：教材 p.220，平行间隙Couette流近似。
eta=0.366
du=1
delta=1e-3

# 求解：黏性耗散是体积热源，不是轴承总功率。
phi=eta*(du/delta)**2
q_area=phi*delta

# 输出
print(f'体积生热率 Φ={phi:.6g} W/m³，单位润滑间隙面积耗散={q_area:.6g} W/m²')
print('轴承总耗散功率还需要润滑间隙面积或体积。')
