import numpy as np

X = np.array([
    ["A", 85, 90, 88],
    ["B", 70, 75, 72],
    ["C", 95, 92, 96]
])

print(X)
print("Shape: ", str(X.shape))
print("Number of rows: ", str(len(X)))
print("Number of columns: ", str(len(X[0])))
print("Transpose: ", X.T)