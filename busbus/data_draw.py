import matplotlib
import matplotlib.pyplot as plt
import numpy as np

t = np.array([1, 2, 3, 4])
s = np.array([0.88777, 0.9222, 0.969999, 0.93222])

fig, ax = plt.subplots(figsize=(5, 3))
# ax.plot(t, s, 'k-', linewidth=1)
ax.errorbar(t, s-0.01, yerr=[0.034, 0.023, 0.01, 0.02], fmt='b^--', ecolor='r', elinewidth=2, capsize=4)
ax.set_yticks([0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0])
ax.set_xticks([1, 2, 3, 4])
ax.set(xlabel='Bus crowdedness level', ylabel='Accuracy')
ax.grid()

fig.savefig("test.png")
plt.show()
