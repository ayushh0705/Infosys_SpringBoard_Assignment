import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = {
    "Age": [22, 25, 30, 35, 40, 45, 50, 55, 60, 65],
    "Salary": [25000, 28000, 35000, 40000, 50000, 60000, 70000, 80000, 85000, 90000]
}

df = pd.DataFrame(data)

X = df[["Age"]]
y = df["Salary"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X)

plt.scatter(df["Age"], df["Salary"], color='blue')
plt.plot(df["Age"], y_pred, color='red')
plt.xlabel("Age")
plt.ylabel("Salary")
plt.title("Simple Linear Regression: Age vs Salary")
plt.show()
