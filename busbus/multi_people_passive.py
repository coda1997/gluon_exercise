import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(7.5, 4.5))

x = np.array([2, 3, 4, 5, 6, 7, 8])

y_3 = np.array([0.95999, 0.961213, 0.96854, 0.96174, 0.97999, 0.97315, 0.97011])
y_4 = np.array([0.91222, 0.92779, 0.94917, 0.94583, 0.95222, 0.97315, 0.97011])
ax.plot(x, y_3 - 0.01, 'm*--', label='Bus Crowdedness Level 3', linewidth=2)
ax.plot(x, y_4 - 0.01, 'gs--', label='Bus Crowdedness Level 4', linewidth=2)
ax.set_yticks([0.8, 0.85, 0.9, 0.95, 1.0])
ax.set_xticks([1, 2, 3, 4, 5, 6, 7, 8])

ax.set(xlabel='The number of participant passengers', ylabel='Accuracy')
legend = ax.legend(shadow=True, fontsize='x-large')
ax.grid()
plt.show()
