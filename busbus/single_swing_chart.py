import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(7.5, 4.5))

x = np.array([1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])
x_3 = np.array([1, 1.5, 2, 2.5, 3, 3.5, 4])
x_4 = np.array([1, 1.5, 2, 2.5, 3])
y_1 = np.array([0.85377, 0.87015, 0.90854, 0.91998, 0.91052, 0.90971, 0.92177, 0.87679, 0.85887])
y_2 = np.array([0.8992, 0.90919, 0.91173, 0.928, 0.93997, 0.9452, 0.91763, 0.91318, 0.9215])
y_3 = np.array([0.95999, 0.961213, 0.96854, 0.96174, 0.97999, 0.97315, 0.97011])
y_4 = np.array([0.91222, 0.92779, 0.94917, 0.94583, 0.95222])
ax.plot(x, y_1-0.01, 'ro--', label='Bus Crowdedness Level 1', linewidth=2)
ax.plot(x, y_2-0.01, 'b^--', label='Bus Crowdedness Level 2', linewidth=2)
ax.plot(x_3, y_3-0.01, 'm*--', label='Bus Crowdedness Level 3', linewidth=2)
ax.plot(x_4, y_4-0.01, 'gs--', label='Bus Crowdedness Level 4', linewidth=2)
ax.set_yticks([0.8, 0.85, 0.9, 0.95, 1.0])
ax.set_xticks([1, 2, 3, 4])

ax.set(xlabel='The Swing variance of Passengers(m)', ylabel='Accuracy')
legend = ax.legend(shadow=True, fontsize='x-large')
ax.grid()
plt.show()
