import numpy as np
def sigmoid(x):
    return 1 / (1 + np.e**(-x))

print(f"{sigmoid(-5)} \n{sigmoid(0)} \n{sigmoid(5)}")