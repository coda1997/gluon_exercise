import numpy as np
from matplotlib import pyplot as plt

t = np.array([1, 2, 3, 4])
s = np.array([0.88777, 0.9222, 0.969999, 0.93222])
dy = 0.043
plt.errorbar(t, s, yerr=dy, fmt='o', ecolor='r', color='b', elinewidth=2, capsize=4)
plt.show()
