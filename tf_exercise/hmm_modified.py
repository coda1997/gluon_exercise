import numpy as np


class HMM:
    def __init__(self, ann):
        self.A = np.array(ann, np.float)
        self.N = self.A.shape[1]
        self.T = self.A.shape[0]
        self.Pi = 1 / self.N

    def viterbi(self):
        # given O,lambda .finding I

        T = self.T
        I = np.zeros(T, np.int)

        delta = np.zeros((T, self.N), np.float)
        psi = np.zeros((T, self.N), np.float)

        for i in range(self.N):
            delta[0, i] = self.Pi[i] * 1
            psi[0, i] = 0

        for t in range(1, T):
            for i in range(self.N):
                delta[t, i] = 1 * np.array([delta[t - 1, j] * self.A[t, j, i]
                                            for j in range(self.N)]).max()
                psi[t, i] = np.array([delta[t - 1, j] * self.A[t, j, i]
                                      for j in range(self.N)]).argmax()

        P_T = delta[T - 1, :].max()
        I[T - 1] = delta[T - 1, :].argmax()

        for t in range(T - 2, -1, -1):
            I[t] = psi[t + 1, I[t + 1]]

        return I
