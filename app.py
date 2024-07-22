
from flask import Flask, render_template, request, jsonify
import requests
import logging

app = Flask(__name__)


logging.basicConfig(level=logging.DEBUG)


MODEL_API_URL = 'http://localhost:5000/predict'  # Ensure this is correct for your API

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
       
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

        
        app.logger.debug(f'Sending data to model API: {data}')

        
        response = requests.post(MODEL_API_URL, json=data)
        
      
        app.logger.debug(f'API response: {response.text}')

        response.raise_for_status()  

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

