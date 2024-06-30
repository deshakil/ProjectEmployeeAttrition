# ProjectEmployeeAttrition
This project aims to predict employee attrition using a machine learning model deployed as an API. The frontend application allows users to input employee data and get predictions on whether the employee is likely to leave the company.

## Table of Contents

- [Project Overview](#project-overview)
- [Tech Stack](#tech-stack)
- [Dataset](#dataset)
- [Model Training](#model-training)
- [API](#api)
- [Frontend](#frontend)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [License](#license)

## Project Overview

This project uses a machine learning model to predict employee attrition based on various factors like age, daily rate, distance from home, hourly rate, monthly income, monthly rate, number of companies worked, total working years, and years at the company.

## Tech Stack

- **Backend**: Flask, Scikit-learn
- **Frontend**: HTML, CSS, Bootstrap
- **Machine Learning**: RandomForestClassifier
- **Deployment**: Flask, Gunicorn

## Model Training

The model is trained using the following features:
- Age
- Daily Rate
- Distance From Home
- Hourly Rate
- Monthly Income
- Monthly Rate
- Number of Companies Worked
- Total Working Years
- Years at Company

The RandomForestClassifier from Scikit-learn is used to train the model.

## API

The backend API is built using Flask and exposes an endpoint to predict employee attrition.

### Endpoint

- **POST /predict**: Predicts whether an employee will leave the company.

#### Request
    ```json
    {
  "Age": 35,
  "DailyRate": 800,
  "DistanceFromHome": 10,
  "HourlyRate": 50,
  "MonthlyIncome": 5000,
  "MonthlyRate": 20000,
  "NumCompaniesWorked": 3,
  "TotalWorkingYears": 10,
  "YearsAtCompany": 5
   }

### Response
     ```json
  {
  "prediction": 1,
  "probability": [0.45, 0.55]
        }


## Frontend
The frontend is built using HTML, CSS, and Bootstrap. It provides a form for users to input employee data and get predictions.

## Setup and Installation
### Prerequisites
    - Python 3.x
    - Flask
    - Scikit-learn
    - Joblib

### Installation
1. Clone the repository
    ```bash
git clone https://github.com/deshakil/ProjectEmployeeAttrition.git
cd <Your-Project-Directory>

2. Create and activate a virtual environment
    ```bash
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate

3. Install the dependencies
    ```bash
pip install -r requirements.txt

4. Run the Machine Learning Model API
    ```bash
python api.py

5. Run the Flask Frontend Application
    ```bash
python app.py

### Usage

1. Start the machine learning model API:
   ```bash
python api.py

2. Start the frontend application :
   ```bash
python app.py

3. Open a web browser and go to http://localhost:5001.

4. Fill out the form with the required employee data and submit it to get the prediction.

### File Structure

    ```plain text
EmployeeAttritionModelAPI/
│
├── app.py                   # Flask frontend application
├── api.py                   # Machine learning model API
├── employee_attrition.pkl   # Trained machine learning model
├── requirements.txt         # Python dependencies
├── templates/
│   ├── index.html           # Home page with input form
│   ├── result.html          # Result page to display predictions
│   └── error.html           # Error page for handling errors
└── static/
    └── style.css            # Custom CSS for styling the frontend

### License
This project is licensed under the MIT License - see the LICENSE file for details.

