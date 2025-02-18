#Student Performance Prediction
import numpy as np
import matplotlib.pyplot as plt
#data points (Study Hours)
x = np.array([1, 2, 3, 4, 5])
#actural output (marks can be obtained based on study our)
y = np.array([10, 20, 30, 40, 50])

m = 0
b = 0
learning_rate = 0.05
iterations = 1000

n = len(x)

for _ in range(iterations):
    y_pred = m * x + b

    dm = -(2 / n) * np.sum(x * (y - y_pred))
    db = -(2 / n) * np.sum(y - y_pred)

    m -= learning_rate * dm
    b -= learning_rate * db

print(f"Final slope (m): {m:.2f}")
print(f"Final intercept (b): {b:.2f}")

def predict(hours):
    return m * hours + b

plt.scatter(x, y, color='blue', label='Actual Data')
plt.plot(x, predict(x), color='red', label='Best-fit Line')
plt.xlabel('Hours Studied')
plt.ylabel('Exam Score')
plt.title('Student Performance Prediction')
plt.legend()
plt.show()

study_hours = 5
predicted_score = predict(study_hours)
print(f"Predicted exam score for studying {study_hours} hours daily: {predicted_score:.2f}")

'''

x = np.array([1, 2, 3, 4, 5])
y = np.array([10, 20, 30, 40, 50])

  observation
  when lr = 0.01
      iteratins = 1000
  O/P for
      7 hours : 69.92
      5 hours : 49.97

  when lr = 0.1
      iteratins = 1000
  O/P for
      7 hours : -219316
      5 hours : -1590

  when lr = 0.01
      iteratins = 100
  O/P for
      7 hours : 68.28
      5 hours : 49.29

  when lr = 0.5
      iteratins = 1000
  O/P for
      7 hours : 70
      5 hours : 50

'''
