# 📘 Day 02 – Matrices & Dataset Representation

## 📅 Date
25-02-2026

---

## 🎯 Objective
Understand how datasets are represented as matrices and implement matrix operations.

---

## 📚 Concepts Covered

### 🔹 Matrix Representation in ML
- Rows represent data samples.
- Columns represent features.
- ML models perform matrix multiplication internally.

### 🔹 Matrix Multiplication
Used to compute predictions in linear models.

### 🔹 Transpose
Converts rows to columns and vice versa.
Useful in gradient descent and advanced ML math.

---

## 💻 Implementation

### Created Dataset Matrix

```python
import numpy as np

X = np.array([
    [21, 20000, 1],
    [25, 35000, 3],
    [30, 60000, 7]
])

### Manual Matrix Multiplication

```python
def matrix_multiply(A, B):
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result

### NumPy Multiplication

```python
np.dot(A, B)

## 📊 Observations

> Manual implementation deepened understanding.
> NumPy is highly optimized.
> Shape mismatches cause common ML errors.

## 🚀 Challenges Faced

> Understanding dimension compatibility.
> Solved by checking .shape before multiplication.

## 🧠 Key Takeaways

> ML models are mathematical matrix operations.
> Understanding shapes prevents future debugging issues.
> Matrix multiplication is the backbone of ML.
