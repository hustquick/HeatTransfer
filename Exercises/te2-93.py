import numpy as np
from scipy.special import iv
import matplotlib.pyplot as plt

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
plt.savefig('./te2-93.pdf')
plt.show()

