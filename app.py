from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

app = Flask(__name__)

# Global model variable
model = None

def train_model():
    global model
    df = pd.read_csv("USA_Housing.csv")
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

    print("Model trained successfully.")

# Train model on startup
train_model()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        income = float(request.form['income'])
        house_age = float(request.form['house_age'])
        rooms = float(request.form['rooms'])
        bedrooms = float(request.form['bedrooms'])
        population = float(request.form['population'])

        input_data = pd.DataFrame([{
            'Income': income,
            'House_Age': house_age,
            'Rooms': rooms,
            'Bedrooms': bedrooms,
            'Population': population
        }])

        predicted_price = model.predict(input_data)[0]

        return render_template('result.html', predicted_price=f"${predicted_price:.2f}")

if __name__ == '__main__':
    app.run(debug=True)
