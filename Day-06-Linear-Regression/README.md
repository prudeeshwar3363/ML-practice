# 📘 Day 06 – Linear Regression From Scratch

## 📅 Date  
01-03-2026

---

## 🎯 Objective

To build a complete Linear Regression model from scratch using Gradient Descent and understand the full training workflow of a supervised learning algorithm.

---

## 🧠 Concepts Learned

### 🔹 Linear Regression Model

- Understood the mathematical equation:
  
  y = wx + b  

- Learned how weight (w) controls slope.
- Learned how bias (b) shifts the line vertically.
- Understood how the model predicts continuous values.

---

### 🔹 Full Training Workflow

Learned the complete machine learning pipeline:

1. Initialize parameters  
2. Compute predictions  
3. Calculate cost (MSE)  
4. Compute gradients  
5. Update parameters  
6. Repeat for multiple iterations  

This iterative process forms the core of supervised learning.

---

### 🔹 Optimization Behavior

- Observed cost decreasing over iterations.
- Saw how weights gradually move toward optimal values.
- Understood convergence behavior of Gradient Descent.
- Learned that more iterations improve optimization but cannot fix model limitations.

---

### 🔹 Perfect vs Noisy Data

- Verified that perfectly linear data leads to near-exact parameter convergence.
- Understood that noisy data results in approximation, not perfection.
- Learned that Linear Regression finds the “best fit line,” not a perfect line.

---

## 🛠 What I Did Today

- Designed and implemented a custom LinearRegression class.
- Implemented training using Gradient Descent.
- Created predict() functionality.
- Trained model on linear dataset.
- Observed parameter convergence.
- Compared results with sklearn’s LinearRegression.
- Verified that learned parameters closely matched library implementation.
- Visualized regression line against actual data points.

---

## 📊 Observations

- Weight converged very close to expected value.
- Bias approached ideal intercept.
- Cost reduced consistently with iterations.
- Model behaved as expected for perfectly linear data.
- sklearn results validated correctness of implementation.

---

## 🚀 Key Realizations

- Linear Regression is fundamentally an optimization problem.
- Gradient Descent drives learning.
- Library implementations are built on the same mathematical foundation.
- Model performance depends on both data quality and model capacity.
- Increasing iterations improves convergence, not model complexity.

---

## 🧠 Challenges Faced

- Managing vector operations correctly.
- Ensuring correct gradient sign.
- Understanding convergence behavior.
- Debugging learning rate issues.

---

## 🔜 Next Step

Move to multivariate linear regression and understand how multiple features influence predictions.

---

## 💡 Reflection

Today was a major milestone in my ML journey.

I successfully built a full supervised learning model from scratch and verified its correctness against a professional library implementation. This strengthened my understanding of optimization, model structure, and training dynamics.

This is where machine learning shifted from theory to engineering.
