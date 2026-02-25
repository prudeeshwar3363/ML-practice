import numpy as np

def matrix_multiply(A, B):
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

A = np.array([
    [8, 9, 8],
    [7, 5, 2],
    [5, 2, 6]
])
B = np.array([
    [5, 10, 8],
    [7, 7, 2],
    [9, 9, 9]
])

print(matrix_multiply(A, B))
print(np.dot(A, B))