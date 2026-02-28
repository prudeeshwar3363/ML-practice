import numpy as np

X = np.array([1, 2, 3])
y = np.array([2, 4, 6])

w = 0.0 
b = 0.0
learning_rate = 0.01
n = len(X)

for i in range(100):
    y_pred = w * X + b
    cost = np.mean((y - y_pred)**2)
    dJ_dw = -(2/n) * np.sum(X * (y - y_pred))
    dJ_db = -(2/n) * np.sum(y - y_pred)
    w = w - learning_rate * dJ_dw
    b = b - learning_rate * dJ_db
    
    print(f"Iteration {i+1}: w={round(w,4)}, b={round(b,4)}, cost={round(cost,4)}")
    
print("w =",round(w, 4))
print("b =",round(b, 4))

