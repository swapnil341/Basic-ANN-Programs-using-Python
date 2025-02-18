#Tempreature Prediction
import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 5, 10, 15, 20])
y = np.array([30, 25, 20, 15, 10])

m = 0
b = 0
learning_rate = 0.001
iterations = 9000

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
plt.xlabel('Altitude')
plt.ylabel('Temperature')
plt.title('Temperature Prediction')
plt.legend()
plt.show()

altitude = 30
predicted_temperature = predict(altitude)
print(f"Predicted temperature at {altitude} meters: {predicted_temperature:.2f}°C")

'''
Observation

x = np.array([0, 5, 10, 15, 20])
y = np.array([30, 25, 20, 15, 10])

  when lr = 0.001
      iteratins = 9000
  O/P for
      10 hours : 19.97°C
      30 hours : 0.08°C

  when lr = 0.01
      iteratins = 9000
  O/P for
      10 hours : nan°C
      30 hours : nan°C

  when lr = 0.001
      iteratins = 1000
  O/P for
      10 hours : 14.89°C
      30 hours : 15.48°C

'''
