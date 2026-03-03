import numpy as np

y = np.array([1, 0, 1])
p = np.array([0.8, 0.3, 0.6])

def log_loss(y, p):
    print(np.log(p))
    return -np.mean(y * np.log(p) + (1 - y) * np.log(1 - p))

print(log_loss(y, p))