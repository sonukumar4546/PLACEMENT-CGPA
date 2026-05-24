
import os
import logging
from flask import Flask, render_template, request
import pickle
import pandas as pd
import numpy as np


# Configure logging (basic setup for app-level messages, not database logs)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__, template_folder='templates')

# Load the model and scaler
model_path = 'cgpa_model.pkl'
scaler_path = 'cgpa_scaler.pkl'

# Load model
with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)

# Load scaler (if you actually used one during training)
scaler = None
if os.path.exists(scaler_path):
    with open(scaler_path, 'rb') as scaler_file:
        scaler = pickle.load(scaler_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # 1. Get input
        cgpa_val = float(request.form['cgpa'])

        # Add validation for CGPA range (3 to 10)
        if not (3.0 <= cgpa_val <= 10.0):
            return render_template('index.html', prediction_text='Invalid CGPA. Please enter a value between 3.0 and 10.0.')

        # 2. Prepare input for prediction
        input_data = pd.DataFrame({'cgpa': [cgpa_val]})

        # 3. Scaling Logic (CRITICAL)
        if scaler:
            try:
                final_input = scaler.transform(input_data)
            except:
                final_input = scaler.transform([[cgpa_val]])
        else:
            final_input = input_data

        # 4. Predict
        prediction = model.predict(final_input)[0]

        if isinstance(prediction, (np.ndarray, list)):
            prediction = prediction[0]

        return render_template('index.html', prediction_text=f'Predicted Package: {prediction:.2f} LPA')

    except ValueError:
        return render_template('index.html', prediction_text='Invalid CGPA. Please enter a numeric value.')
    except Exception as e:
        return render_template('index.html', prediction_text=f'An error occurred: {str(e)}')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
