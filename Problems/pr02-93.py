import numpy as np
from scipy.special import iv
import matplotlib.pyplot as plt
import os
import sys
sys.path.append("..")
from Functions.Self_defined import save_pdf

delta = 0.0001
x = np.linspace(delta, 2.5, 1000)
mH = np.sqrt(2) * x
I_0 = iv(0, 2*mH)
I_1 = iv(1, 2*mH)
I_2 = iv(2, 2*mH)
eta = 2 / mH * I_2 / I_1
fig, ax = plt.subplots()
ax.plot(x, eta)
ax.set_xlabel('$x$')
ax.set_ylabel('$\eta(x)$')
name = os.path.basename(__file__).split(".")[0]
save_pdf(name, plt)

