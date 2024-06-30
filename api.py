from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load('employee_attrition.pkl')

# Assume you have the same data columns as used during training
data_columns = ['Age', 'DailyRate', 'DistanceFromHome', 'HourlyRate', 'MonthlyIncome', 
                'MonthlyRate', 'NumCompaniesWorked', 'TotalWorkingYears', 
                'YearsAtCompany']

@app.route('/')
def home():
    return "Employee Attrition Prediction API"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        
        # Ensure data has all required columns
        if not all(col in data for col in data_columns):
            return jsonify({'error': 'Missing data columns or incorrect format'}), 400

        # Extract the features and convert to numpy array
        features = np.array([data[col] for col in data_columns]).reshape(1, -1)

        # Make prediction (without scaling)
        prediction = model.predict(features)
        prediction_proba = model.predict_proba(features)

        return jsonify({
            'prediction': int(prediction[0]),
            'probability': prediction_proba[0].tolist()
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True,port=5000)