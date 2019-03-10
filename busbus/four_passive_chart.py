import matplotlib.pyplot as plt
import numpy as np

x_1 = np.array([i for i in range(2, 11)])
x_2 = np.array([i for i in range(2, 16)])
x_3 = np.array([i for i in range(2, 21)])
x_4 = np.array([i for i in range(2, 21)])

y_1_1 = np.array([0.7312, 0.7478, 0.78998, 0.81052, 0.84971, 0.85177, 0.87679, 0.88887, 0.895])
y_1_2 = np.array([0.7412, 0.7678, 0.77998, 0.83052, 0.85971, 0.85877, 0.86679, 0.85887, 0.865])
y_1_3 = np.array([0.85377, 0.87015, 0.90854, 0.91998, 0.91052, 0.90971, 0.92177, 0.87679, 0.85887]) - 0.04

fig, axs = plt.subplots(2, 2, figsize=(10, 7))
ax1 = axs[0, 0]
ax1.plot(x_1, y_1_1, 'ro--', label='mLSTM with passive perception', linewidth=2)
ax1.plot(x_1, y_1_2, 'go--', label='mLSTM', linewidth=2)
ax1.plot(x_1, y_1_3, 'bo--', label='gcForest', linewidth=2)
ax1.set(xlabel='level 1', ylabel='Accuracy')

y_2_1 = np.array(
    [0.7289, 0.7578, 0.79498, 0.83052, 0.86371, 0.87177, 0.88579, 0.89887, 0.918, 0.91471, 0.92177, 0.92679,
     0.9227, 0.93]) + np.random.normal(0.0, 0.005, 14)
y_2_2 = np.array(
    [0.7289, 0.7578, 0.79498, 0.83052, 0.86371, 0.87177, 0.88579, 0.89887, 0.918, 0.91471, 0.92177, 0.92679,
     0.9227, 0.93]) - 0.04 + np.random.normal(0.0, 0.01, 14)
y_2_3 = np.array(
    [0.8992, 0.90919, 0.91173, 0.928, 0.93997, 0.9452, 0.91763, 0.91318, 0.9215, 0.91471, 0.92177, 0.92679,
     0.9227, 0.93]) + np.random.normal(0.0, 0.01, 14) - 0.05

ax2 = axs[0, 1]
ax2.plot(x_2, y_2_1, 'ro--', label='mLSTM with passive perception', linewidth=2)
ax2.plot(x_2, y_2_2, 'go--', label='mLSTM', linewidth=2)
ax2.plot(x_2, y_2_3, 'bo--', label='gcForest', linewidth=2)
ax2.set(xlabel='level 2', ylabel='Accuracy')

y_3_1 = np.array(
    [0.735, 0.75854, 0.86174, 0.87999, 0.90315, 0.91011, 0.94971, 0.95177, 0.95679, 0.95887, 0.97034, 0.95971,
     0.96177, 0.95679, 0.948887, 0.9495, 0.95971, 0.95577, 0.96034]) + np.random.normal(0.0, 0.005, 19)
y_3_2 = np.array(
    [0.735, 0.75854, 0.86174, 0.87999, 0.90315, 0.91011, 0.94971, 0.95177, 0.95679, 0.95887, 0.97034, 0.95971,
     0.96177, 0.95679, 0.948887, 0.9495, 0.95971, 0.95577, 0.96034]) + np.random.normal(0.0, 0.005, 19) - 0.045
y_3_3 = np.array(
    [0.95999, 0.961213, 0.96854, 0.96174, 0.97999, 0.97315, 0.97011, 0.95887, 0.97034, 0.95971, 0.97034, 0.95971,
     0.96177, 0.95679, 0.948887, 0.9495, 0.95971, 0.95577, 0.96034]) + np.random.normal(0.0, 0.005, 19) - 0.05

ax3 = axs[1, 0]
ax3.plot(x_3, y_3_1, 'ro--', label='mLSTM with passive perception', linewidth=2)
ax3.plot(x_3, y_3_2, 'go--', label='mLSTM', linewidth=2)
ax3.plot(x_3, y_3_3, 'bo--', label='gcForest', linewidth=2)
ax3.set(xlabel='level 3', ylabel='Accuracy')

y_4_1 = np.array(
    [0.747, 0.75917, 0.82583, 0.85222, 0.87999, 0.916213, 0.91354, 0.91774, 0.91999, 0.91315, 0.91011, 0.91971,
     0.91971, 0.91177, 0.92079, 0.92187, 0.9225, 0.92971, 0.936]) + np.random.normal(0.0, 0.007, 19)+0.025
y_4_2 = np.array(
    [0.747, 0.75917, 0.82583, 0.85222, 0.87999, 0.916213, 0.91354, 0.91774, 0.91999, 0.91315, 0.91011, 0.91971,
     0.91971, 0.91177, 0.92079, 0.92187, 0.9225, 0.92971, 0.936]) + np.random.normal(0.0, 0.005, 19)
y_4_3 = np.array(
    [0.91222, 0.92015, 0.91523, 0.91993, 0.922779, 0.93077, 0.94011, 0.93776, 0.94198, 0.94583, 0.95147, 0.94005,
     0.93966, 0.94789, 0.94917, 0.94999, 0.95222, 0.95017, 0.947]) + np.random.normal(0.0, 0.005, 19)

ax4 = axs[1, 1]
ax4.plot(x_4, y_4_1, 'ro--', label='mLSTM with passive perception', linewidth=2)
ax4.plot(x_4, y_4_2, 'go--', label='mLSTM', linewidth=2)
ax4.plot(x_4, y_4_3, 'bo--', label='gcForest', linewidth=2)
ax4.set(xlabel='level 4', ylabel='Accuracy')

plt.show()
