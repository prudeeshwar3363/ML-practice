import numpy as np
import matplotlib.pyplot as plt

salary = [20000, 35000, 60000, 80000, 120000]
def mean(arr):
    return sum(arr)/len(arr)
def standard_deviation(arr):
    return ((sum([(arr[i]-(sum(arr)/len(arr)))**2 for i in range(len(arr))]))/(len(arr)))**0.5

mean = mean(salary)
standard_deviation = standard_deviation(salary)

def standardization(arr):
    return [round((i-mean)/standard_deviation, 2) for i in arr]

transformed_salary = standardization(salary)
print(transformed_salary)

plt.figure()
plt.plot(salary)
plt.title("Original Salary")
plt.xlabel("Index")
plt.ylabel("Salary")
plt.show()

plt.figure()
plt.plot(transformed_salary)
plt.title("standardized Salary")
plt.xlabel("Index")
plt.ylabel("standardized Salary")
plt.show()