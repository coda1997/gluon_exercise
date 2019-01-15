# In[0]
import pymongo
import numpy as np
import csv
import math

# connect to the database
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["rotation"]
cols = mydb["datas_arm_weight_training_wrist"]


def get_locations_from_database(q0, q1, q2, q3, error):
    res = cols.find({"q0": {"$gt": q0 - error, "$lt": q0 + error},
                     "q1": {"$gt": q1 - error, "$lt": q1 + error},
                     "q2": {"$gt": q2 - error, "$lt": q2 + error},
                     "q3": {"$gt": q3 - error, "$lt": q3 + error}
                     })
    if res.count() == 0:
        return get_locations_from_database(q0, q1, q2, q3, error + 0.06)
    else:
        print(res.count())
        return res


def rotation_matrix_to_quaternions(R):
    tr = R[0][0] + R[1][1] + R[2][2]
    quaternisons = [0.0, 0.0, 0.0, 0.0]
    if tr > 0:
        quaternisons[0] = math.sqrt(1 + tr) / 2
        quaternisons[1] = (R[2][1] - R[1][2]) / quaternisons[0] / 4
        quaternisons[2] = (R[0][2] - R[2][0]) / quaternisons[0] / 4
        quaternisons[1] = (R[1][0] - R[0][1]) / quaternisons[0] / 4
    else:
        max = np.max([R[0][0], R[1][1], R[2][2]])
        if max == R[0][0]:
            t = math.sqrt(1 + R[0][0] - R[1][1] - R[2][2])
            quaternisons[0] = (R[2][1] - R[1][2]) / t
            quaternisons[1] = t / 4
            quaternisons[2] = (R[0][2] + R[2][0]) / t
            quaternisons[3] = (R[0][1] + R[1][0]) / t
        if max == R[1][1]:
            t = math.sqrt(1 - R[0][0] + R[1][1] - R[2][2])
            quaternisons[0] = (R[0][2] - R[2][0]) / t
            quaternisons[1] = (R[0][1] + R[1][0]) / t
            quaternisons[2] = t / 4
            quaternisons[3] = (R[2][1] + R[1][2]) / t
        if max == R[2][2]:
            t = math.sqrt(1 - R[0][0] - R[1][1] + R[2][2])
            quaternisons[0] = (R[1][0] - R[0][1]) / t
            quaternisons[1] = (R[0][2] + R[2][0]) / t
            quaternisons[2] = (R[1][2] - R[2][1]) / t
            quaternisons[3] = t / 4

    return quaternisons


def find_locations(rotation_matrix):
    Q = rotation_matrix_to_quaternions(rotation_matrix)
    error = 0.05
    res = get_locations_from_database(Q[0], Q[1], Q[2], Q[3], error)
    Q = np.array(Q)
    dist = 10000
    loc = ""
    for r in res:
        q0 = r["q0"]
        q1 = r["q1"]
        q2 = r["q2"]
        q3 = r["q3"]
        temp = np.array([q0, q1, q2, q3])
        distance = np.sum((temp - Q) ** 2)
        if dist > distance:
            dist = distance
            loc = r["loc"]
    return loc_string_to_array(loc)


def loc_string_to_array(loc):
    ress = loc[1:-1].split(',')
    num = int(len(ress) / 3)
    res = np.zeros(shape=(num, 3))
    for i in range(0, num):
        res[i][0] = float(ress[3 * i].strip().lstrip('[').rstrip(']'))
        res[i][1] = float(ress[3 * i + 1].strip().lstrip('[').rstrip(']'))
        res[i][2] = float(ress[3 * i + 2].strip().lstrip('[').rstrip(']'))
    print(res)
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

# locs = np.array((10, -1, 3))
locations = []
_temp = 0
for row in csv_reader:
    # if N > 10:  # 11 times
    #     break
    # N = N + 1

    if len(row) == 7:
        rot = romatrix(float(row[6]), float(row[5]), float(row[3]))
        rot_list = rot.tolist()
        res = find_locations(rot_list)
        locations.append(res)

# In[1]

T = len(locations) - 1
delta_T = 0.1

# initialize states
# states = np.zeros(shape=(T, N, 3))
states = []
for i in range(0, T):
    loc_1 = locations[i]
    loc_2 = locations[i + 1]
    len_row = len(loc_1)
    len_col = len(loc_2)
    states.append([0.0 for i in range(0, len_row * len_col)])
    for row in range(0, len_row):
        for col in range(0, len_col):
            states[i][row * len_col + col] = (loc_1[row] - loc_2[col]) / delta_T

# dummy observed acc
res = np.zeros(shape=(T, 3))
acc_observed = 0
# Initialization state

# probs = np.zeros(shape=(T, N))
# updating from 1 to T
probs = [[0 for i in range(0, len(states[0]))]]
for t in range(0, T - 1):
    state_from = states[t]
    state_to = states[t + 1]
    tag = 0
    min = 1000000
    probs.append([0 for i in range(0, len(state_to))])
    for col in range(0, len(state_to)):
        min_temp = 1000000
        for row in range(0, len(state_from)):
            if row % 3 == col / 3:
                acc = (state_to[col] - state_from[row]) / delta_T
                temp = np.sum((acc - acc_observed) ** 2)
                temp_probs = probs[t][row] + temp
                if temp_probs < min_temp:
                    probs[t + 1][col] = temp_probs

        if probs[t + 1][col] < min:
            min = probs[t + 1][col]
            tag = col
    rr_len = len(locations[t + 2])
    tag = tag % rr_len
    print(locations[t + 2][tag])
    res[t + 1] = locations[t + 2][tag]

out = open("res-wrist.csv", "a+", newline="")
csv_writer = csv.writer(out, dialect="excel")

for t in range(1, len(res)):
    csv_writer.writerow(res[t])
