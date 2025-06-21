import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error

df = pd.read_csv("C:/Users/athin/OneDrive/Desktop/AI projects/USA_Housing.csv")

df = df.dropna()
df = df.drop('Address', axis=1)
df = df.rename(columns={
    'Avg. Area Income': 'Income',
    'Avg. Area House Age': 'House_Age',
    'Avg. Area Number of Rooms': 'Rooms',
    'Avg. Area Number of Bedrooms': 'Bedrooms',
    'Area Population': 'Population'
})

x = df.drop('Price', axis=1)
y = df['Price']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

print(f"Predicted: {y_pred[:5]}") 
print(f"Actual: {y_test.values[:5]}")

r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f"R² Score: {r2:.4f}")
print(f"RMSE: {rmse:.4f}\n\n")

value = pd.DataFrame([{
    'Income': int(input('Enter Income: ')),
    'House_Age': int(input('House Age: ')),
    'Rooms': int(input('No od rooms: ')),
    'Bedrooms': int(input('No of bedrooms: ')),
    'Population': int(input('Population: '))
}])

predicted_price = model.predict(value)
print(f"Predicted Price for house: ${predicted_price[0]:.2f}")