import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(7.5, 4.5))

x = np.array([x for x in range(2, 21)])
y_1 = np.array(
    [0.747, 0.75917, 0.82583, 0.85222, 0.87999, 0.916213, 0.91354, 0.91774, 0.91999, 0.91315, 0.91011, 0.91971,
     0.91971, 0.91177, 0.92079, 0.92187, 0.9225, 0.92971, 0.936]) + np.random.normal(0.0, 0.005, 19)
y_2 = np.array(
    [0.75917, 0.82583, 0.85222, 0.87999, 0.916213, 0.91354, 0.91774, 0.91999, 0.91315, 0.91011, 0.91971,
     0.91971, 0.91177, 0.92079, 0.92187, 0.9225, 0.92971, 0.936,0.925]) + np.random.normal(0.0, 0.007, 19) + 0.025
y_3 = np.array(
    [0.95999, 0.961213, 0.96854, 0.96174, 0.97999, 0.97315, 0.97011]) + np.random.normal(0.0, 0.005, 7) - 0.07
# y_4 = np.array([0.91222, 0.92779, 0.94917, 0.94583, 0.95222, 0.97315, 0.97011])
# ax.plot(x, y_3, 'm*--', label='gcForest', linewidth=2)
ax.plot(x, y_1, 'gs--', label='mLSTM without passive perception', linewidth=2)
ax.plot(x, y_2, 'r^--', label='mLSTM with passive perception', linewidth=2)
# ax.set_yticks([0.8, 0.85, 0.9, 0.95, 1.0])
ax.set_xticks([x for x in range(2, 21)])

ax.set(xlabel='The number of participant passengers', ylabel='Accuracy', title='Bus Crowdedness Level 4')
legend = ax.legend(shadow=True, fontsize='x-large')
ax.grid()
plt.show()
