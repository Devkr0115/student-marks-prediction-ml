import pandas as pd

from sklearn.linear_model import LinearRegression

# Read dataset
data = pd.read_csv("data/student_scores.csv")

# Features and Target
X = data[['Hours']]
y = data['Marks']

# Train model on complete dataset
model = LinearRegression()
model.fit(X, y)

print("===== Student Marks Prediction =====")

hours = float(input("Enter Study Hours: "))

new_data = pd.DataFrame({
    "Hours": [hours]
})

prediction = model.predict(new_data)

print(f"\nPredicted Marks: {prediction[0]:.2f}")