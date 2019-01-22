import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(7.5, 4.5))

x = np.array([i for i in range(2, 21)])
x_1 = np.array([i for i in range(2, 11)])
x_2 = np.array([i for i in range(2, 16)])

o_1 = [0.72, 0.895]
o_2 = [0.73, 0.93]
o_3 = [0.735, 0.97]
o_4 = [0.747, 0.936]

y_1 = np.array([0.7312, 0.7478, 0.78998, 0.81052, 0.84971, 0.85177, 0.87679, 0.88887, 0.895])
y_2 = np.array(
    [0.7289, 0.7578, 0.79498, 0.83052, 0.85371, 0.87177, 0.88579, 0.89887, 0.918, 0.91471, 0.92177, 0.92679,
     0.9227, 0.93])
y_3 = np.array(
    [0.735, 0.96854, 0.96174, 0.97999, 0.97315, 0.97011, 0.84971, 0.85177, 0.87679, 0.87887, 0.895, 0.88971,
     0.89177, 0.89679, 0.908887, 0.9295, 0.94971, 0.96177, 0.97034])
y_4 = np.array(
    [0.747, 0.94917, 0.94583, 0.95222, 0.95999, 0.961213, 0.96854, 0.96174, 0.97999, 0.97315, 0.97011,0.84971,
     0.84971, 0.85177, 0.87679, 0.88887, 0.895, 0.84971, 0.936])
ax.plot(x_1, y_1, 'ro--', label='Bus Crowdedness Level 1', linewidth=2)
ax.plot(x_2, y_2, 'b^--', label='Bus Crowdedness Level 2', linewidth=2)
ax.plot(x, y_3, 'm*--', label='Bus Crowdedness Level 3', linewidth=2)
ax.plot(x, y_4, 'gs--', label='Bus Crowdedness Level 4', linewidth=2)
ax.set_yticks([0.7, 0.8, 0.9, 1.0])
ax.set_xticks([i for i in range(1, 21)])

ax.set(xlabel='Number of participant passengers on the bus', ylabel='Accuracy')
legend = ax.legend(shadow=True, fontsize='x-large')
ax.grid()
plt.show()
