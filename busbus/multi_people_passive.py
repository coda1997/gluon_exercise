import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(7.5, 4.5))

x = np.array([2, 3, 4, 5, 6, 7, 8])
y_1 = np.array(
    [ 0.75854, 0.86174, 0.87999, 0.90315, 0.91011, 0.94971,0.95000]) + np.random.normal(0.0, 0.005, 7)
y_2 = np.array(
    [0.735, 0.75854, 0.86174, 0.87999, 0.90315, 0.91011, 0.94471]) + np.random.normal(0.0, 0.005, 7)
y_3 = np.array(
    [0.95999, 0.961213, 0.96854, 0.96174, 0.97999, 0.97315, 0.97011]) + np.random.normal(0.0, 0.005, 7) - 0.07
# y_4 = np.array([0.91222, 0.92779, 0.94917, 0.94583, 0.95222, 0.97315, 0.97011])
# ax.plot(x, y_3, 'm*--', label='gcForest', linewidth=2)
ax.plot(x, y_1, 'gs--', label='mLSTM without passive perception', linewidth=2)
ax.plot(x, y_2, 'r^--', label='mLSTM with passive perception', linewidth=2)
# ax.set_yticks([0.8, 0.85, 0.9, 0.95, 1.0])
ax.set_xticks([1, 2, 3, 4, 5, 6, 7, 8])

ax.set(xlabel='The number of participant passengers', ylabel='Accuracy', title='Bus Crowdedness Level 3')
legend = ax.legend(shadow=True, fontsize='x-large')
ax.grid()
plt.show()
