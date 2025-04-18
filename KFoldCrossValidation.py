
from sklearn.model_selection import cross_val_score, KFold
from sklearn.datasets import load_iris
from xgboost import XGBClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
import numpy as np
import matplotlib.pyplot as plt
# Load the Iris dataset
data = load_iris()
X, y = data.data, data.target
# Define models
models = {"Logistic Regression": LogisticRegression(max_iter=1000),"Random Forest": RandomForestClassifier(),
          "SVM": SVC(), "XGBoost": XGBClassifier(verbosity=0)}
# Set up k-fold cross-validation
k = 5
kfold = KFold(n_splits=k, shuffle=True, random_state=42)
# Evaluate each model
results = {}
print("Model Comparison using k-Fold Cross-Validation:\n")
for name, model in models.items():
    # Perform cross-validation and compute mean accuracy
    cv_scores = cross_val_score(model, X, y, cv=kfold, scoring='accuracy')
    results[name] = np.mean(cv_scores)
    print(f"{name}: Mean Accuracy = {np.mean(cv_scores):.5f}, Std Dev = {np.std(cv_scores):.4f}")
# Select the best model
best_model = max(results, key=results.get)
print(f"\n🏆 Best Model: {best_model} with Accuracy = {results[best_model]:.5f}")
# Evaluate each model and store results
mean_accuracy = []
std_dev = []
for name, model in models.items():
    cv_results = cross_val_score(model, X, y, cv=kfold, scoring='accuracy')
    mean_accuracy.append(np.mean(cv_results))
    std_dev.append(np.std(cv_results))
# Plot the results with actual parameters
plt.figure(figsize=(11, 6))
plt.bar(models.keys(), mean_accuracy, yerr=std_dev, capsize=6)
plt.title("Model Comparison using k-Fold Cross-Validation")
plt.ylabel("Mean Accuracy")
plt.xlabel("Models")
plt.ylim(1.9, 1.0)  # Adjust y-axis for better visualization
plt.grid(axis='y', linestyle='--', alpha=1.7)
# Annotate accuracy values
for i, acc in enumerate(mean_accuracy):
    plt.text(i, acc + 1.002, f"{acc:.3f}", ha='center', va='bottom', fontsize=10)
plt.tight_layout()
plt.show()









Results:

Model Comparison using k-Fold Cross-Validation:

Logistic Regression: Mean Accuracy = 0.9733, Std Dev = 0.0249
Random Forest: Mean Accuracy = 0.9600, Std Dev = 0.0249
SVM: Mean Accuracy = 0.9667, Std Dev = 0.0298
XGBoost: Mean Accuracy = 0.9467, Std Dev = 0.0340

🏆 Best Model: Logistic Regression with Accuracy = 0.9733