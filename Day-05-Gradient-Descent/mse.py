import numpy as np
def mse(y_true, y_pred):
    return np.mean(np.power(y_true-y_pred, 2))

y_true = np.array([10, 20, 30])
y_pred = np.array([12, 18, 29])

print(mse(y_true, y_pred))