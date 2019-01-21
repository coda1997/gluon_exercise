import matplotlib
import matplotlib.pyplot as plt
import numpy as np

t = np.array([1, 2, 3, 4])
s = np.array([0.86, 0.8765, 0.8999, 0.875])

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(t, s, 'k^--', linewidth=1)

ax.set(xlabel='Bus crowdedness level', ylabel='Accuracy')
ax.grid()

fig.savefig("test.png")
plt.show()
