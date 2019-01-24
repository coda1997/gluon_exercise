import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

out = open("res-elbow.csv")
reader = csv.reader(out)
loc = []
xs = []
ys = []
zs = []
for row in reader:
    x = float(row[0])
    y = float(row[1])
    z = float(row[2])
    xs.append(x)
    ys.append(y)
    zs.append(z)
    loc.append([x, y, z])

for i in loc:
    print(i)

fig = plt.figure()
ax = Axes3D(fig)
# plt.scatter(ys, zs)
ax.scatter(xs, ys, zs)
plt.savefig('fig.png', bbox_inches='tight')
plt.show()
