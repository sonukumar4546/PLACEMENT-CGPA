
import os
from flask import Flask, render_template, request
import pickle
import pandas as pd
import numpy as np

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

        # 2. Prepare input for prediction
        # If your model was trained on a DataFrame, keep this.
        # If it was trained on a raw array, use np.array([[cgpa_val]])
        input_data = pd.DataFrame({'cgpa': [cgpa_val]})

        # 3. Scaling Logic (CRITICAL)
        # Only scale if you used scaler.transform() on your training data before LR.fit()
        if scaler:
            # Check if feature names match; if not, use a simple array
            try:
                final_input = scaler.transform(input_data)
            except:
                final_input = scaler.transform([[cgpa_val]])
        else:
            final_input = input_data

        # 4. Predict
        prediction = model.predict(final_input)[0]

        # If it's a 2D array result, grab the first element
        if isinstance(prediction, (np.ndarray, list)):
            prediction = prediction[0]

        return render_template('index.html', prediction_text=f'Predicted Package: {prediction:.2f} LPA')

    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
