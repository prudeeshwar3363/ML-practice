import numpy as np

# manual implementation of mean, variance and standard deviation
def mean(arr):
    return sum(arr)/len(arr)
def variance(arr):
    return (sum([(arr[i]-(sum(arr)/len(arr)))**2 for i in range(len(arr))]))/(len(arr))
def standard_deviation(arr):
    return ((sum([(arr[i]-(sum(arr)/len(arr)))**2 for i in range(len(arr))]))/(len(arr)))**0.5

m1 = mean([1,2,3,4,5])
v1 = variance([1,2,3,4,5])
s1 = standard_deviation([1,2,3,4,5])

print("Manual Mean:", m1)
print("Manual Variance:", v1)
print("Manual Standard Deviation:", s1)

# numpy implementation
m2 = np.mean([1,2,3,4,5])
v2 = np.var([1,2,3,4,5])
s2 = np.std([1,2,3,4,5])

print("Numpy Mean:", m2)
print("Numpy Variance:", v2)
print("Numpy Standard Deviation:", s2)

# comparing the results
if m1 == m2 and v1 == v2 and s1 == s2:
    print("Manual Implementation is same as Numpy Implementation")
else:
    print("Manual Implementation is not same as Numpy Implementation")