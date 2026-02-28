import numpy as np

X = np.array([1, 2, 3])
y = np.array([2, 4, 6])

w = 0
b = 0
learning_rate = 0.01

y_pred = np.sum(np.dot(w, X), b)
cost = np.subtract(y, y_pred)
dJ_dw = np.mean(np.multiply(-2, np.dot(X, cost)))
dJ_db = np.mean(np.multiply(-2, np.sum(cost)))

w = w - learning_rate * dJ_dw
b = b - learning_rate * dJ_db

print(w, b)

