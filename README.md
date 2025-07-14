# Shopper Purchase Prediction App

A Flask web application that predicts whether an online shopper will make a purchase based on their browsing behavior and session characteristics.

## Files Included

- `app.py` - Main Flask application
- `main.py` - Entry point for running the application
- `templates/index.html` - Web interface with prediction form
- `shopper_model.joblib` - Pre-trained machine learning model
- `README.md` - This file

## How to Run

1. Install dependencies:
   ```bash
   pip install flask joblib numpy scikit-learn
   ```

2. Run the application:
   ```bash
   python main.py
   ```

3. Open your browser and go to `http://localhost:5000`

## Features

- 17 input fields for shopper behavior metrics
- Machine learning prediction (Yes/No for purchase)
- Clean, simple web interface
- Error handling for invalid inputs

## Input Fields

The model expects 17 features:
1. Administrative pages visited
2. Administrative duration
3. Informational pages visited
4. Informational duration
5. Product-related pages visited
6. Product-related duration
7. Bounce rates
8. Exit rates
9. Page values
10. Special day indicator
11. Month (1-12)
12. Operating system ID
13. Browser ID
14. Region ID
15. Traffic type ID
16. Visitor type (1=Returning, 0=New/Other)
17. Weekend indicator (1=Yes, 0=No)

## Deployment

This app is ready to deploy on platforms like:
- Replit
- Heroku
- PythonAnywhere
- Any Flask-compatible hosting service