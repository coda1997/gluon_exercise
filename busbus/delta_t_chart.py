import matplotlib.pyplot as plt

name_list = ['2', '4', '6', '8']
num_list = [1.5, 0.6, 7.8, 6]
num_list_1 = [1, 2, 3, 4]
num_list_2 = [1, 2, 3, 4]

x = list(range(len(num_list)))
total_width, n = 1.6, 4
width = total_width / n

plt.bar(x, num_list, width=width, label='head', fc='b')
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, num_list_1, width=width, label='middle', tick_label=name_list, fc='r')
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, num_list_2, width=width, label='tail', tick_label=name_list, fc='g')
plt.xlabel('interval time in second')
plt.ylabel('accuracy')
plt.legend()
plt.show()
