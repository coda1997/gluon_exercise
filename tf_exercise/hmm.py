import numpy as np


class HMM:
    def __init__(self, Ann, Bnm, Pi, O):
        self.A = np.array(Ann, np.float)
        self.B = np.array(Bnm, np.float)
        self.Pi = np.array(Pi, np.float)
        self.O = np.array(O, np.int)
        self.N = self.A.shape[1]
        self.M = self.B.shape[1]

    def viterbi(self):
        # given O,lambda .finding I

        T = len(self.O)
        I = np.zeros(T, np.int)

        delta = np.zeros((T, self.N), np.float)
        psi = np.zeros((T, self.N), np.float)

        for i in range(self.N):
            delta[0, i] = self.Pi[i] * self.B[i, self.O[0]]
            psi[0, i] = 0

        for t in range(1, T):
            for i in range(self.N):
                delta[t, i] = self.B[i, self.O[t]] * np.array([delta[t - 1, j] * self.A[t, j, i]
                                                               for j in range(self.N)]).max()
                psi[t, i] = np.array([delta[t - 1, j] * self.A[t, j, i]
                                      for j in range(self.N)]).argmax()

        P_T = delta[T - 1, :].max()
        I[T - 1] = delta[T - 1, :].argmax()

        for t in range(T - 2, -1, -1):
            I[t] = psi[t + 1, I[t + 1]]

        return I
