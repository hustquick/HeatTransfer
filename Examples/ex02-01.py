import sys
from pathlib import Path

project_root = str(Path(__file__).resolve().parents[1])
if project_root not in sys.path:
    sys.path.insert(0, project_root)
from Appendix.Appendix4_lambda_ import get_lambda_

material = '水泥珍珠岩制品'
rho = 300
delta = 120e-3
t1 = 500
t2 = 50
tau = 1 * 3600

t_m = (t1 + t2) / 2
lambda_m = get_lambda_(material, t_m)
q = lambda_m * (t1 - t2) / delta * tau
print(f'q = {q:.2f} J/m^2')
