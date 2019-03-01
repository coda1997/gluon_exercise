import matplotlib.pyplot as plt
import numpy as np

x_1 = np.array([i for i in range(1, 11)])
x_2 = np.array([i for i in range(1, 16)])
x_3 = np.array([i for i in range(1, 21)])
x_4 = np.array([i for i in range(1, 21)])

y_1_1 = np.array([0.7312, 0.7478, 0.78998, 0.81052, 0.84971, 0.85177, 0.87679, 0.88887, 0.895, 0.093])
y_1_2 = np.array([0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5])
y_1_3 = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

fig, axs = plt.subplots(2, 2, figsize=(10, 7))
ax1 = axs[0, 0]
ax1.plot(x_1, y_1_1, 'ro--', label='mLSTM with passive perception', linewidth=2)
ax1.plot(x_1, y_1_2, 'ro--', label='mLSTM', linewidth=2)
ax1.plot(x_1, y_1_3, 'ro--', label='gcForest', linewidth=2)
ax1.set(xlabel='level 1', ylabel='Accuracy')

ax2 = axs[0, 1]
ax2.plot(np.random.rand(100))
ax2.set(xlabel='level 2', ylabel='Accuracy')

ax3 = axs[1, 0]
ax3.plot(np.random.rand(100))
ax3.set(xlabel='level 3', ylabel='Accuracy')

ax4 = axs[1, 1]
ax4.plot(np.random.rand(100))
ax4.set(xlabel='level 4', ylabel='Accuracy')

plt.show()
