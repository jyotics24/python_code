# Import required libraries
from flask import Flask, request, jsonify, render_template
import joblib  # For loading the saved ML model

# Create Flask app instance
app = Flask(__name__)

# Load the trained Logistic Regression model
model = joblib.load('model.pkl')

# Route for homepage — renders HTML form
@app.route('/')
def home():
    return render_template('index.html')

# Route for prediction — triggered on form submission
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract form input values, convert to float, and store in a list
        data = [float(request.form[key]) for key in [
            'Gender', 'Age', 'Smoker', 'BP_Med', 'P_Stroke', 'Hypertension',
            'Diabetes', 'Cholesterol', 'Systolic_Bp', 'BMI', 'Heart_rate', 'Glucose'
        ]]

        # Predict using the model
        prediction = model.predict([data])[0]

        # result based on prediction
        result = "You Are at Risk of Heart Disease." if prediction == 1 else "You Are Not at Risk of Heart Disease."

        # Render result back to HTML page
        return render_template('index.html', prediction_text=result)

    except Exception as e:
        # Return error info as JSON if something goes wrong
        return jsonify({'error': str(e)})

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)