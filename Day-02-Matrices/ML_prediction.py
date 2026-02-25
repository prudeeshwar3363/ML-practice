import numpy as np

X = np.array([
    [85, 90, 88],
    [70, 75, 72],
    [95, 92, 96]
])

W = np.array([0.3, 0.4, 0.3])

pridiction_result = np.dot(X, W)
print(pridiction_result)