# 📘 Day 08 – Logistic Regression (Binary Classification)

## 📅 Date  
03-03-2026

---

## 🎯 Objective

To understand the fundamentals of Logistic Regression, including the sigmoid function, probability interpretation, log-loss (binary cross-entropy), and decision boundary concepts.

---

## 🧠 Concepts Learned

### 🔹 Classification vs Regression

- Understood the difference between predicting continuous values (regression) and categorical outcomes (classification).
- Learned that Logistic Regression is used for binary classification problems.
- Realized that probabilities must lie between 0 and 1, unlike linear regression outputs.

---

### 🔹 Sigmoid Function

- Studied the sigmoid function:
  
  σ(z) = 1 / (1 + e^(-z))

- Learned how it maps any real number into the range (0,1).
- Observed how:
  - Large positive inputs → output close to 1
  - Large negative inputs → output close to 0
  - Zero input → output = 0.5
- Understood its role in converting linear outputs into probabilities.

---

### 🔹 Linear Equation Inside Logistic Regression

- Learned that logistic regression still uses a linear equation:
  
  z = wx + b

- The sigmoid function is applied on this linear combination.
- Understood how the decision boundary occurs when z = 0.

---

### 🔹 Log Loss (Binary Cross Entropy)

- Learned why Mean Squared Error is not ideal for classification.
- Studied the log-loss function:

  J = -1/n Σ [ y log(p) + (1 - y) log(1 - p) ]

- Understood:
  - Confident wrong predictions are penalized heavily.
  - Log-loss ensures convex optimization.
  - Loss increases sharply when predicted probability contradicts the true label.

---

### 🔹 Decision Boundary

- Derived decision boundary formula:
  
  wx + b = 0

- Understood how this separates two classes.
- Learned how slope and intercept define classification regions.

---

## 🛠 What I Did Today

- Implemented the sigmoid function and tested it with positive, negative, and zero inputs.
- Computed linear combination (z = wx + b) manually.
- Converted linear outputs into probabilities using sigmoid.
- Implemented binary log-loss from scratch.
- Calculated decision boundary analytically.
- Interpreted probability outputs for classification decisions.

---

## 📊 Observations

- Sigmoid smoothly transforms linear outputs into probabilities.
- Log-loss penalizes incorrect high-confidence predictions strongly.
- Logistic regression is still a linear model at its core.
- Decision boundary depends only on the linear equation (not sigmoid directly).

---

## 🚀 Key Realizations

- Logistic regression predicts probability, not class directly.
- Classification happens by applying a threshold (usually 0.5).
- Convex cost surface ensures stable convergence.
- Logistic regression is the foundation for neural network classification.

---

## 🧠 Challenges Faced

- Understanding why MSE is unsuitable for classification.
- Interpreting probability outputs in decision-making.
- Grasping how log-loss penalizes confident mistakes.

---

## 🔜 Next Step

Implement full Logistic Regression using Gradient Descent and evaluate classification accuracy.

---

## 💡 Reflection

Today marked the transition from regression to classification.  
I now understand how probabilities are generated using sigmoid and why log-loss is necessary for stable optimization.  
This strengthened my understanding of how classification models learn and how decision boundaries are formed.
