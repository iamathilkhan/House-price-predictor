# 🏡 USA Housing Price Predictor - Linear Regression

This project uses a **linear regression** model to predict housing prices based on various socioeconomic and geographic features from the USA Housing dataset.

---

## 🔍 Project Overview

- **Goal**: Predict the price of a house based on input features.
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
- Pandas
- NumPy
- Scikit-learn

---

## 📊 Model Evaluation

- **R² Score**: ~0.91 (very high fit)
- **RMSE**: ~100,000 (depends on unit scale of prices)

---

## 📥 How to Use

1. Clone the repo or download the `.py` file.
2. Make sure `USA_Housing.csv` is present in the same folder or update the file path.
3. Run the script:
   ```bash
   python linear_model.py
