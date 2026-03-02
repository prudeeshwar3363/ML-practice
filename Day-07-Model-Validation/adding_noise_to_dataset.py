import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

X = np.array([1, 2, 3, 4, 5])
y = np.array([2.1, 3.9, 6.2, 7.8, 10.1])

class CustomLinearRegression():
    def __init__(self, learning_rate=10, n_iters=10, w=0, b=0):
        self.learning_rate = learning_rate
        self.n_iters = n_iters
        self.w = w
        self.b = b

    def fit(self, X, y):
        n = len(X)
        for _ in range(self.n_iters):
            y_pred = self.w * X + self.b
            error = y - y_pred
            dJ_dw = (-2/n) * np.sum(X * error)
            dJ_db = (-2/n) * np.sum(error)
            self.w = self.w - self.learning_rate * dJ_dw
            self.b = self.b - self.learning_rate * dJ_db
    def predict(self, X):
        if (self.w is None) or (self.b is None):
            raise RuntimeError("The model has not been fitted yet. Call fit() first.")
        else:
            return self.w * X + self.b
def main():
    model = CustomLinearRegression()
    model.fit(X, y)
    print("--- Custom Model Results ---")
    print(f"Weight (w): {model.w:.4f}")
    print(f"Bias (b): {model.b:.4f}")

    # Using scikit-learn's model for comparison
    # Renamed variable to avoid overwriting the imported class
    sk_model = LinearRegression()
    sk_model.fit(X.reshape(-1, 1), y)
    print("\n--- Scikit-learn Model Results ---")
    print(f"Coefficient (w): {sk_model.coef_[0]:.4f}")
    print(f"Intercept (b): {sk_model.intercept_:.4f}")

    plt.scatter(X, y, label='Data')
    plt.plot(X, model.predict(X), color='red', label='Custom Model Fit')
    plt.title("Linear Regression Fit")
    plt.legend()
    plt.show()
# It's good practice to wrap executable code in a main block.
if __name__ == "__main__":
    main()