# 🏡 USA Housing Price Predictor - Flask Web App

This project is a **Flask web application** that uses a **linear regression** model to predict housing prices based on various socioeconomic and geographic features from the USA Housing dataset.

---

## 🔍 Project Overview

- **Goal**: Predict the price of a house based on input features via a web interface.
- **Algorithm**: Linear Regression
- **Dataset**: `USA_Housing.csv` (commonly available from public datasets or platforms like Kaggle)

---

## 🧠 Features Used

The model uses the following features to predict housing price:

- `Income`: Average Area Income
- `House_Age`: Average Age of Houses in the Area
- `Rooms`: Average Number of Rooms
- `Bedrooms`: Average Number of Bedrooms
- `Population`: Area Population

---

## 🛠 Technologies Used

- Python
- Flask
- Pandas
- NumPy
- Scikit-learn

---

## 📊 Model Evaluation

- **R² Score**: ~0.91 (very high fit)
- **RMSE**: ~100,000 (depends on unit scale of prices)

---

## 🚀 How to Run

1. Clone the repo or download the files.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Make sure `USA_Housing.csv` is present in the same folder.
4. Run the Flask app:
   ```bash
   python app.py
   ```
5. Open your browser and go to `http://127.0.0.1:5000/`

---

## 🌐 Web Interface

- **Home Page**: Form to input house features
- **Prediction Page**: Displays the predicted price

---

## 📁 Project Structure

```
House-price-predictor/
├── app.py                 # Flask application
├── linear.py              # Original script
├── USA_Housing.csv        # Dataset
├── requirements.txt       # Dependencies
├── templates/
│   ├── index.html         # Input form
│   └── result.html        # Prediction result
└── README.md              # This file
```
