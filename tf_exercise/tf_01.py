from tf_exercise.hmm import HMM
import numpy as np
import pandas as pd

# data = pd.read_csv('result.txt')
#
# for r in data.nrows():
#     print(r)

N = 20
# Ann : shape(T,n,n), is a list of 2D n by n matrix. T: the number of timestamps
Ann = [[[0.5, 0.2, 0.3], [0.3, 0.5, 0.2], [0.2, 0.3, 0.5]], [[0.5, 0.2, 0.3], [0.3, 0.5, 0.2], [0.2, 0.3, 0.5]],
       [[0.5, 0.2, 0.3], [0.3, 0.5, 0.2], [0.2, 0.3, 0.5]]]  # update Ann

Bnm = [[0.5, 0.5], [0.4, 0.6], [0.7, 0.3]]
pi = [0.2, 0.4, 0.4]
O = np.zeros(len(Ann))

hmm = HMM(Ann, Bnm, pi, [0, 1, 0])
I = hmm.viterbi()
print(I)
