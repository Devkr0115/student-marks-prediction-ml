# Student Marks Prediction Using Machine Learning

## Project Description

This project predicts a student's marks based on the number of study hours using the **Linear Regression** algorithm. It demonstrates the basic workflow of Machine Learning, including data preprocessing, model training, prediction, evaluation, and visualization.

---

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Matplotlib

---

## Features

- Predicts student marks based on study hours
- Uses the Linear Regression algorithm
- Splits data into training and testing sets
- Evaluates the model using Mean Absolute Error (MAE)
- Visualizes the regression line using Matplotlib
- Accepts user input to predict marks

---

## Project Structure

```text
student-marks-prediction-ml/
│
├── data/
│   └── student_scores.csv
├── model.py
├── predict.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
https://github.com/Devkr0115/student-marks-prediction-ml.git
```

Navigate to the project folder:

```bash
cd student-marks-prediction-ml
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

## How to Run

### Train and Evaluate the Model

```bash
python model.py
```

This will:

- Load the dataset
- Train the Linear Regression model
- Evaluate the model
- Display the Mean Absolute Error (MAE)
- Show the regression graph

### Predict Student Marks

```bash
python predict.py
```

Example:

```text
===== Student Marks Prediction =====

Enter Study Hours: 7

Predicted Marks: 73.43
```

---

## Machine Learning Workflow

1. Load the dataset
2. Separate features and target values
3. Split the dataset into training and testing sets
4. Train the Linear Regression model
5. Make predictions
6. Evaluate model performance using MAE
7. Visualize the regression line

