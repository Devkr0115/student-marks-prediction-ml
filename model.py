import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Read the dataset
data = pd.read_csv("data/student_scores.csv")

print("First 5 Rows:\n")
print(data.head())

print("\nDataset Information:\n")
print(data.info())

# Features (Input) and Target (Output)
X = data[['Hours']]
y = data['Marks']

print("\nFeatures (X):")
print(X.head())

print("\nTarget (y):")
print(y.head())

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Samples:", len(X_train))
print("Testing Samples:", len(X_test))

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

print("\nModel Trained Successfully!")

print("\nSlope (Coefficient):", model.coef_[0])
print("Intercept:", model.intercept_)

# Predict on test data
y_pred = model.predict(X_test)

print("\nActual Marks:")
print(y_test.values)

print("\nPredicted Marks:")
print(y_pred)

# Evaluate model
mae = mean_absolute_error(y_test, y_pred)

print("\nMean Absolute Error:", mae)

# Draw Graph
plt.figure(figsize=(8,5))

plt.scatter(X, y, color="blue", label="Actual Data")
plt.plot(X, model.predict(X), color="red", linewidth=2, label="Regression Line")

plt.title("Student Marks Prediction using Linear Regression")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.legend()

plt.show()