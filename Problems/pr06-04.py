from CoolProp.CoolProp import PropsSI as psi


# 已知条件：教材p.276，同通道、同速度、均为湍流；氢气采用题给物性。
T,p=323.15,101300
rho_H,k_H,eta_H,cp_H=.0755,.1942,9.41e-6,14360
rho_A=psi('D','T',T,'P',p,'Air')
k_A=psi('L','T',T,'P',p,'Air')
eta_A=psi('V','T',T,'P',p,'Air')
cp_A=psi('C','T',T,'P',p,'Air')
Pr_H=eta_H*cp_H/k_H
Pr_A=eta_A*cp_A/k_A

# 求解：以Dittus–Boelter比较h，未知u和d在比值中消去。
for n,label in [(.4,'气体被加热'),(.3,'气体被冷却')]:
 ratio=k_H/k_A*((rho_H/eta_H)/(rho_A/eta_A))**.8*(Pr_H/Pr_A)**n
 print(f'{label}：h_氢/h_空气={ratio:.6f}')

# 输出
print(f'Pr_氢={Pr_H:.6f}，Pr_空气={Pr_A:.6f}')
print('结果只针对相同速度和几何的湍流对流；不等同于同泵功下的整机效率。')
