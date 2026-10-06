import sys
from pathlib import Path

project_root = str(Path(__file__).resolve().parents[1])
if project_root not in sys.path:
    sys.path.insert(0, project_root)
from Functions.UnsteadyStateConduction import get_a, Q_s_for_constant_t_w

t_0 = 50
t_w = 20
tau = 10*60
rho = 2300
c = 880
lambda_ = 1.4

a = get_a(lambda_, rho, c)
Q = Q_s_for_constant_t_w(tau, t_0, t_w, lambda_, a)
print(f'Q = {-Q:.0f} J')
print('这一假设使计算得到的放热偏高')
