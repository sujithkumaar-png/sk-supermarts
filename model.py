# model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error
import pickle

def train_model():
    # Sample data for training - Replace with your actual data
    # This assumes a CSV file with columns: product_id, day_of_week, month, year, sales
    data = pd.DataFrame({
        'product_id': [101, 102, 103, 104],
        'day_of_week': [1, 2, 3, 4],
        'month': [1, 2, 3, 4],
        'year': [2022, 2022, 2022, 2022],
        'sales': [200, 300, 250, 400]
    })

    X = data[['product_id', 'day_of_week', 'month', 'year']].values
    y = data['sales'].values

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the SVM model
    model = SVR(kernel='linear')
    model.fit(X_train, y_train)

    # Test model performance
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Model MSE: {mse}")

    # Save the trained model
    with open('svm_model.pkl', 'wb') as file:
        pickle.dump(model, file)

if __name__ == "__main__":
    train_model()
