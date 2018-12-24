# In[0]
import pymongo
import numpy as np
import csv
import math
from tf_exercise.hmm_modified import HMM

# connect to the database
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["rotation"]
cols = mydb["datas"]


def find_locations(rotation_matrix):
    rot0 = round(rotation_matrix[0][0], 4)
    rot1 = round(rotation_matrix[0][1], 4)
    rot2 = round(rotation_matrix[0][2], 4)
    rot3 = round(rotation_matrix[1][0], 4)
    rot4 = round(rotation_matrix[1][1], 4)
    rot5 = round(rotation_matrix[1][2], 4)
    rot6 = round(rotation_matrix[2][0], 4)
    rot7 = round(rotation_matrix[2][1], 4)
    rot8 = round(rotation_matrix[2][2], 4)
    error = 0.05
    rotation_matrix = np.reshape(rotation_matrix, 9)
    res = cols.find({"rot0": {"$gt": rot0 - error, "$lt": rot0 + error},
                     "rot1": {"$gt": rot1 - error, "$lt": rot1 + error},
                     "rot2": {"$gt": rot2 - error, "$lt": rot2 + error},
                     "rot3": {"$gt": rot3 - error, "$lt": rot3 + error},
                     "rot4": {"$gt": rot4 - error, "$lt": rot4 + error},
                     "rot5": {"$gt": rot5 - error, "$lt": rot5 + error},
                     "rot6": {"$gt": rot6 - error, "$lt": rot6 + error},
                     "rot7": {"$gt": rot7 - error, "$lt": rot7 + error},
                     "rot8": {"$gt": rot8 - error, "$lt": rot8 + error}
                     })
    dist = 10000
    loc = ""
    for r in res:
        rot0 = r["rot0"]
        rot1 = r["rot1"]
        rot2 = r["rot2"]
        rot3 = r["rot3"]
        rot4 = r["rot4"]
        rot5 = r["rot5"]
        rot6 = r["rot6"]
        rot7 = r["rot7"]
        rot8 = r["rot8"]
        temp = np.array([rot0, rot1, rot2, rot3, rot4, rot5, rot6, rot7, rot8])
        distance = np.sum((temp - rotation_matrix) ** 2)
        if dist > distance:
            dist = distance
            loc = r["loc"]
    print(loc)
    return loc_string_to_array(loc)


def loc_string_to_array(loc):
    ress = loc[1:-1].split(',')
    num = int(len(ress) / 3)
    res = np.zeros(shape=(num, 3))
    for i in range(0, num):
        res[i][0] = float(ress[3 * i])
        res[i][1] = float(ress[3 * i + 1])
        res[i][2] = float(ress[3 * i + 2])
    return res


def romatrix(a1, a2, a3):
    sinZ = np.sin(a1)
    sinX = np.sin(a2)
    sinY = np.sin(a3)

    cosZ = np.cos(a1)
    cosX = np.cos(a2)
    cosY = np.cos(a3)
    xM = [[1, 0, 0], [0, cosX, sinX], [0, -sinX, cosX]]

    xM = np.mat(xM)
    yM = [[cosY, 0, sinY], [0, 1, 0], [-sinY, 0, cosY]]
    yM = np.mat(yM)
    zM = [[cosZ, sinZ, 0], [-sinZ, cosZ, 0], [0, 0, 1]]
    zM = np.mat(zM)

    R = zM * xM * yM
    world2watch = np.linalg.inv(R)
    body2world = [[-1, 0, 0], [0, 0, -1], [0, -1, 0]]
    body2world = np.mat(body2world)
    R = body2world * world2watch
    R = np.round(R, 2)
    return R


csv_reader = csv.reader(open('5.csv', encoding='utf-8'))

N = 0
locs = np.array((10, -1, 3))
locations = np.zeros(shape=(11, 3, 3))
for row in csv_reader:
    if N > 10:  # 11 times
        break
    N = N + 1

    if len(row) == 7:
        rot = romatrix(float(row[6]), float(row[5]), float(row[3]))
        rot_list = rot.tolist()
        res = find_locations(rot_list)
        locations[N - 1] = res

# In[1]

T = locations.shape[0] - 1
N = locations.shape[2] ** 2
states = np.zeros(shape=(T, N, 3))
delta_T = 0.1
for i in range(0, T):
    loc_1 = locations[i]
    loc_2 = locations[i + 1]
    for row in range(0, len(loc_1)):
        for col in range(0, len(loc_2)):
            states[i, row * 3 + col] = (loc_1[row] - loc_2[col]) / delta_T
Ann = np.zeros(shape=(T - 1, N, N))
acc_observed = np.zeros(shape=(T - 1, 3))
for i in range(0, T - 1):
    state_1 = states[i]
    state_2 = states[i + 1]
    for row in range(0, len(state_1)):
        for col in range(0, len(state_2)):
            if row % 3 == col / 3:
                acc = state_1[row] - state_2[col] / delta_T
                Ann[i, row, col] = 1 / (math.sqrt(2 * math.pi)) * math.exp(np.sum(acc - acc_observed[i] ** 2))
# In[2]
# Ann get
hmm = HMM(ann=Ann)
I = hmm.viterbi()
print(I)
