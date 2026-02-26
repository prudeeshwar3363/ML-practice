# 📘 Day 03 – Statistics for Machine Learning

## 📅 Date
26-02-2026

---

## 🎯 Objective

To understand and implement:

- Mean
- Variance
- Standard Deviation
- Standardization (Z-score normalization)

And understand why feature scaling is critical in Machine Learning.

---

# 📚 Theory Summary

### 🔹 Mean
Represents the central value of the dataset.

\[
\mu = \frac{1}{n} \sum x_i
\]

Used in:
- Normalization
- Cost functions
- Data analysis

---

### 🔹 Variance
Measures how spread out data is from the mean.

\[
\sigma^2 = \frac{1}{n} \sum (x_i - \mu)^2
\]

Higher variance → more spread  
Lower variance → tightly clustered data

---

### 🔹 Standard Deviation
Square root of variance.

\[
\sigma = \sqrt{\sigma^2}
\]

Used in feature scaling.

---

### 🔹 Standardization

\[
z = \frac{x - \mu}{\sigma}
\]

After scaling:
- Mean ≈ 0
- Std ≈ 1

Prevents large features from dominating ML models.

---

# 💻 Task Implementations

---

## 🔹 Task 1 – Manual Mean, Variance, Std

```python
import math

data = [1, 2, 3, 4, 5]

def mean(arr):
    return sum(arr)/len(arr)
def variance(arr):
    return (sum([(arr[i]-(sum(arr)/len(arr)))**2 for i in range(len(arr))]))/(len(arr))
def standard_deviation(arr):
    return ((sum([(arr[i]-(sum(arr)/len(arr)))**2 for i in range(len(arr))]))/(len(arr)))**0.5

m1 = mean(data)
v1 = variance(data)
s1 = standard_deviation(data)

print("Manual Mean:", m1)
print("Manual Variance:", v1)
print("Manual Standard Deviation:", s1)
```

## ✅ Output

```python
Manual Mean: 3.0
Manual Variance: 2.0
Manual Standard Deviation: 1.4142135623730951
```

## 🔹 Task 2 – Compare with NumPy

```python
import numpy as np

print("NumPy Mean:", np.mean(data))
print("NumPy Variance:", np.var(data))
print("NumPy Std:", np.std(data))
```

## ✅ Output

```python
Numpy Mean: 3.0
Numpy Variance: 2.0
Numpy Std: 1.4142135623730951
```
Manual and NumPy outputs match.

## 🔹 Task 3 – Salary Standardization

```python
salary = np.array([20000, 35000, 60000, 80000, 120000])

mean_salary = np.mean(salary)
std_salary = np.std(salary)

standardized_salary = (salary - mean_salary) / std_salary
rounded = [round(v, 2) for v in standardized_salary]

print("Mean:", mean_salary)
print("Standard Deviation:", round(std_salary, 2))
print("Standardized Values:", rounded)
```

## ✅ Output

```python
Mean: 63000.0
Standard Deviation: 35156.79
Standardized Values: [-1.22, -0.8, -0.09, 0.48, 1.62]
```

## 🔹 Task 4 – Post-Scaling Verification

```python
print("Mean after scaling:", round(np.mean(standardized_salary), 5))
print("Std after scaling:", round(np.std(standardized_salary), 5))
```
## ✅ Output

```python
Mean after scaling: 0.0
Std after scaling: 1.0
```

## 📊 Observations

> Manual implementation deepened conceptual clarity.
> Variance measures data spread.
> Standardization centers data at 0 with unit variance.
> Scaling is essential before training ML models.

## 🚀 Challenges Faced

> Understanding why variance squares differences.
> Solved by realizing negative deviations cancel out otherwise.
> Floating point rounding differences observed.

## 🧠 Key Takeaways

> Statistics is foundational for ML.
> Feature scaling prevents bias in model training.
> Understanding math reduces blind reliance on libraries.
