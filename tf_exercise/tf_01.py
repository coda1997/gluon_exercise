import numpy as np
from tf_exercise.tf_hmm import HMMTensorflow


# x_data = np.float32(np.random.rand(2, 100))
# y_data = np.dot([0.100, 0.200], x_data) + 0.300
#
# b = tf.Variable(tf.zeros([1]))
# W = tf.Variable(tf.random_uniform([1, 2], -1.0, 1.0))
# y = tf.matmul(W, x_data) + b
#
# loss = tf.reduce_mean(tf.square(y - y_data))
# optimizer = tf.train.GradientDescentOptimizer(0.5)
# train = optimizer.minimize(loss)
#
# init = tf.initialize_all_variables()
#
# sess = tf.Session()
# sess.run(init)

# for step in range(0, 201):
#     sess.run(train)
#     if step % 20 == 0:
#         print((step, sess.run(W), sess.run(b)))
def lik(y):
    """
    given 1d vector of likliehoods length N, return matrix with
    shape (N, 2) where (N, 0) is 1 - y and (N, 1) is y.
    given a 2d array of likelihood sequences of size [N, B] where B is the batch
    size, return [B, N, 2] where out[B, N, 0] + out[B, N, 1] = 1
    This makes it easy to convert a time series of probabilities
    into 2 states, off/on, for a simple HMM.
    """

    liklihood = np.array([y, y], float).T
    liklihood[..., 0] = 1 - liklihood[..., 0]
    return liklihood


hmmtf = HMMTensorflow(np.array([[0.5, 0.2, 0.3], [0.3, 0.5, 0.2], [0.2, 0.3, 0.5]]), p0=np.array([0.2, 0.4, 0.4]))

tf_s_graph, tf_score_graph = hmmtf.viterbi_decode(lik(np.array([0.5, 0.4, 0.7])))
print(str(tf_s_graph))
print(str(tf_score_graph))
