import matplotlib.pyplot as plt
import numpy as np

# plt.plot([0, 1, 2, 3], [0, 2, 3, 4])
# plt.axis([0, 3, 0, 4])
# plt.ylabel('some numbers')


# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
# plt.axis([0, 6, 0, 20])

# t = np.arange(0., 5., 0.2)
#
# plt.plot(t, t, 'r--', t, t ** 2, 'bs', t, t ** 3, 'g^')

data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()
