import numpy as np

X = np.array([1, 2, 3])
w = 1
b = -2

def computation(X, w, b):
    return np.dot(X, w) + b

def sigmoid(x):
    return 1 / (1 + np.e**(-x))

z = computation(X, w, b)
a = sigmoid(z)

print(f"Z = {z} \nSigmoid(Z) = {a}")