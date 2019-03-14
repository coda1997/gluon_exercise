import math
import numpy as np

data_1 = np.array([0.8919, 0.91897, 0.9575, 0.9202])
data_2 = np.array([0.8919, 0.91897, 0.9575, 0.9202]) - np.random.normal(0.02, 0.02, 4)
data_3 = np.array([0.8919, 0.91897, 0.9575, 0.9202]) + np.random.normal(0.02, 0.02, 4)

print(data_1)
print(data_2)
print(data_3)
