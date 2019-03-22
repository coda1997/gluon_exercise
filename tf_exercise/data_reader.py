import pymongo
import math
import numpy as np
import csv
from timeit import default_timer as timer

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["rotation"]
cols = mydb["datas_arm_weight_training"]


def get_locations_from_database(q0, q1, q2, q3, error):
    locations = cols.find({"q0": {"$gt": q0 - error, "$lt": q0 + error},
                           "q1": {"$gt": q1 - error, "$lt": q1 + error},
                           "q2": {"$gt": q2 - error, "$lt": q2 + error},
                           "q3": {"$gt": q3 - error, "$lt": q3 + error}
                           })
    while locations.count() == 0:
        error += 0.001
        locations = cols.find({"q0": {"$gt": q0 - error, "$lt": q0 + error},
                               "q1": {"$gt": q1 - error, "$lt": q1 + error},
                               "q2": {"$gt": q2 - error, "$lt": q2 + error},
                               "q3": {"$gt": q3 - error, "$lt": q3 + error}
                               })
    if locations.count() > 50:
        locations = locations[0:50]
    return locations


def rotation_matrix_to_quaternions(R):
    tr = R[0][0] + R[1][1] + R[2][2]
    quaternisons = [0.0, 0.0, 0.0, 0.0]
    if tr > 0:
        quaternisons[0] = math.sqrt(1 + tr) / 2
        quaternisons[1] = (R[2][1] - R[1][2]) / quaternisons[0] / 4
        quaternisons[2] = (R[0][2] - R[2][0]) / quaternisons[0] / 4
        quaternisons[1] = (R[1][0] - R[0][1]) / quaternisons[0] / 4
    else:
        max = np.max(([R[0][0], R[1][1], R[2][2]]))
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
    # time_1 = timer()
    Q = rotation_matrix_to_quaternions(rotation_matrix)
    error = 0.01
    res = get_locations_from_database(float(Q[0]), float(Q[1]), float(Q[2]), float(Q[3]), error)
    # Q = np.array(Q)
    loc = ""
    result = []
    for r in res:
        loc = r["loc"]
        loc = loc_string_to_array(loc)
        for l in loc:
            result.append(l)
    # print('find location time %d' % (timer() - time_1))
    return result


def loc_string_to_array(loc):
    ress = loc[1:-1].split(',')
    num = int(len(ress) / 3)
    res = np.zeros((num, 3), dtype="float32")
    for i in range(0, num):
        res[i][0] = float(ress[3 * i].strip().lstrip('[').rstrip(']'))
        res[i][1] = float(ress[3 * i + 1].strip().lstrip('[').rstrip(']'))
        res[i][2] = float(ress[3 * i + 2].strip().lstrip('[').rstrip(']'))
    return res


def romatrix(a1, a2, a3):
    a1 = math.pi / 180 * a1
    a2 = math.pi / 180 * a2
    a3 = math.pi / 180 * a3
    sinZ = math.sin(a1)
    sinX = math.sin(a2)
    sinY = math.sin(a3)

    cosZ = math.cos(a1)
    cosX = math.cos(a2)
    cosY = math.cos(a3)
    xM = [[1, 0, 0], [cosX, sinX, 0], [0, -sinX, cosX]]

    xM = np.mat(xM)
    yM = [[cosY, 0, sinY], [0, 1, 0], [-sinY, 0, cosY]]
    yM = np.mat(yM)
    zM = [[cosZ, sinZ, 0], [-sinZ, cosZ, 0], [0, 0, 1]]
    zM = np.mat(zM)

    R = zM * xM * yM
    world2watch = R
    # world2watch = np.linalg.inv(R)
    body2world = [[0, 1, 0], [0, 0, -1], [-1, 0, 0]]
    body2world = np.mat(body2world)
    R = body2world * world2watch
    R = np.round(R, 2)
    return R


csv_reader = csv.reader(open('3.csv', encoding='utf-8'))
for row in csv_reader:
    if len(row) == 8:
        start_time = timer()
        rot = romatrix(float(row[7]), float(row[6]), float(row[4]))
        res = find_locations(rot)
        print('used time is %d, res number is %d' % (timer()-start_time, len(res)))
