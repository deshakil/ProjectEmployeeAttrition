'''from flask import Flask, request, jsonify
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
    app.run(debug=True) '''

from flask import Flask, render_template, request, jsonify
import requests
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Endpoint URL of your machine learning model API
MODEL_API_URL = 'http://localhost:5000/predict'  # Ensure this is correct for your API

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract data from form submission
        data = {
            'Age': int(request.form['Age']),
            'DailyRate': int(request.form['DailyRate']),
            'DistanceFromHome': int(request.form['DistanceFromHome']),
            'HourlyRate': int(request.form['HourlyRate']),
            'MonthlyIncome': int(request.form['MonthlyIncome']),
            'MonthlyRate': int(request.form['MonthlyRate']),
            'NumCompaniesWorked': int(request.form['NumCompaniesWorked']),
            'TotalWorkingYears': int(request.form['TotalWorkingYears']),
            'YearsAtCompany': int(request.form['YearsAtCompany'])
        }

        # Log the data being sent to the API
        app.logger.debug(f'Sending data to model API: {data}')

        # Make a POST request to the machine learning model API
        response = requests.post(MODEL_API_URL, json=data)
        
        # Log the raw response from the API
        app.logger.debug(f'API response: {response.text}')

        response.raise_for_status()  # Raise an exception for HTTP errors

        response_json = response.json()
        app.logger.debug(f'API response JSON: {response_json}')

        prediction = response_json.get('prediction')
        probability = response_json.get('probability')

        return render_template('result.html', prediction=prediction, probability=probability)

    except requests.exceptions.RequestException as e:
        app.logger.error(f'API request failed: {e}')
        return render_template('error.html', message='API request failed. Please try again later.'), 500

    except ValueError as e:
        app.logger.error(f'ValueError: {e}')
        return render_template('error.html', message='Invalid input. Please check your data and try again.'), 400

    except KeyError as e:
        app.logger.error(f'KeyError: {e}')
        return render_template('error.html', message='Unexpected API response format.'), 500

if __name__ == '__main__':
    app.run(port=5001, debug=True)  # Run the Flask app on port 5001

