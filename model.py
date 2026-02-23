import numpy as np
import pickle
from sklearn.linear_model import LinearRegression

# Simple example: Study Hours vs Marks
X = np.array([[1], [2], [3], [4], [5], [6]])
y = np.array([35, 40, 50, 55, 65, 70])

model = LinearRegression()
model.fit(X, y)

# Save model
pickle.dump(model, open("model.pkl", "wb"))

print("Model trained and saved successfully!")
