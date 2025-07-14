import os
from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('shopper_model.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Fetch form values
        values = [float(x) for x in request.form.values()]
        prediction = model.predict([np.array(values)])
        output = "Yes" if prediction[0] else "No"
        return render_template('index.html', prediction_text=f'Will the shopper make a purchase? {output}')
    except:
        return render_template('index.html', prediction_text='Invalid input. Please check your values.')

if __name__ == '__main__':
    # Use environment variable PORT for port number
    port = int(os.environ.get('PORT', 5000))  # Default to 5000 if PORT is not set
    app.run(host='0.0.0.0', port=port)
