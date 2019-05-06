import numpy as np
import math as math

sigmoid = np.vectorize(lambda x: 1/(1+math.exp(-x)))

def feed_forward(X,theta1,theta2):
    a3 = []
    for i in range(X.shape[0]):
        x = X[i,:].reshape(2,1)
        a1 = np.vstack((1,x))
        z2 = np.matmul(theta1,a1)
        a2 = sigmoid(z2)
        a2 = np.vstack((1,a2))

        z3 = np.matmul(theta2,a2)
        # a3 = sigmoid(z3)
        a3.append(sigmoid(z3))
    return a3

theta1 = np.array([0.1,0.3,0.5,0.2,0.4,0.6]).reshape(2,3) # el weight
theta2 = np.array([0.7,0.8,0.9]).reshape(1,3) # el input
# x = np.array([1,2]).reshape(2,1)
X = np.array([1,2,3,4]).reshape(2,2)
print(
    'h:',
    feed_forward(
        X,
        theta1,
        theta2
    )
)