import sys
from pathlib import Path

project_root = str(Path(__file__).resolve().parents[1])
if project_root not in sys.path:
    sys.path.insert(0, project_root)
from Functions.SteadyStateConduction import fin_tip_R

L = 8e-3
# t_0 = t_L
h = 100
lambda_ = 200
delta = 1e-3
a = 100e-3
b = 200e-3
c = 14e-3

H = L / 2
perimeter = 2 *(a + delta)
A_c = a * delta
R = fin_tip_R(H, perimeter, A_c, lambda_, h)
print(f'每片肋片的热阻为：{R:.2f} W/K')
