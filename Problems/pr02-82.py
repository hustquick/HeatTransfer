import sys
from pathlib import Path

project_root = str(Path(__file__).resolve().parents[1])
if project_root not in sys.path:
    sys.path.insert(0, project_root)
from Functions.SteadyStateConduction import fin_tip_Delta_T_ratio
from sympy import symbols

# H, perimeter, A_c, lambda_, h = symbols('H, perimeter, A_c, lambda_, h')
# Delta_T_ratio = fin_tip_Delta_T_ratio(H, perimeter, A_c, lambda_, h)

