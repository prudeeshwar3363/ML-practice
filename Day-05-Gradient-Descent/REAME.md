# 📘 Day 05 – Cost Function & Gradient Descent

## 📅 Date  
[Enter Date]

---

## 🎯 Objective

To understand how machine learning models learn by minimizing prediction error using a cost function and optimizing parameters through Gradient Descent.

---

## 🧠 Concepts Learned

### 🔹 Cost Function (Mean Squared Error - MSE)

- Learned how to measure model performance using Mean Squared Error.
- Understood why errors are squared:
  - Prevents negative values from canceling positive ones.
  - Penalizes larger errors more heavily.
- Realized that minimizing cost directly improves model accuracy.

---

### 🔹 Model Parameters (Weight & Bias)

- Understood how linear models use:
  - **Weight (w)** to control slope
  - **Bias (b)** to shift the line
- Learned that training involves adjusting these parameters to reduce prediction error.

---

### 🔹 Gradient Descent

- Learned that Gradient Descent is an optimization algorithm used to minimize the cost function.
- Understood the role of:
  - **Gradient** → Direction of steepest increase
  - **Learning Rate** → Step size of updates
- Realized that subtracting the gradient moves parameters toward the minimum error.

---

### 🔹 Learning Rate Behavior

- If too large → Model overshoots minimum (unstable training).
- If too small → Learning becomes very slow.
- Proper learning rate ensures smooth and stable convergence.

---

## 🛠 What I Did Today

- Implemented Mean Squared Error manually.
- Computed prediction errors.
- Derived and calculated gradients for both weight and bias.
- Updated parameters using Gradient Descent formula.
- Ran multiple iterations (100 steps).
- Observed cost decreasing over time.
- Verified that weight converged close to the correct value.

---

## 📊 Observations

- Cost consistently decreased with iterations.
- Weights gradually moved toward optimal solution.
- Gradient direction directly influences parameter updates.
- Training is essentially repeated error correction.

---

## 🚀 Key Realizations

- High-level `.fit()` functions internally perform these exact steps.
- Machine Learning is fundamentally mathematical optimization.
- Gradient Descent removes the “black box” feeling of ML.
- Iterative improvement is core to all supervised learning models.

---

## 🧠 Challenges Faced

- Initially confused between scalar and vector operations.
- Clarified element-wise multiplication vs dot product usage.
- Improved understanding of gradient formula intuition.

---

## 🔜 Next Step

Build a complete Linear Regression model from scratch and train it end-to-end.

---

## 💡 Reflection

Today was a major milestone in my ML journey.

For the first time, I clearly understood how a machine learning model learns and improves through optimization rather than just using pre-built library functions.

This strengthened my mathematical foundation and boosted my confidence in understanding model training mechanics.
