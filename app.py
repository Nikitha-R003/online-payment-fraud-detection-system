from flask import Flask, render_template, request
import joblib

# Initialize the Flask app
app = Flask(__name__,template_folder=r'C:\projectff\template')

# Load the trained Random Forest model
model = joblib.load('random_forest_model.pkl')

# Define the route for the homepage (where the user will see the form)
@app.route('/')
def home():
    return render_template('index.html')

# Define the route for making predictions
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get features from the form input
        feature1 = float(request.form['feature1'])
        feature2 = float(request.form['feature2'])
        feature3 = float(request.form['feature3'])
        feature4 = float(request.form['feature4'])
        feature5 = float(request.form['feature5'])
        feature6 = int(request.form['feature6'])
        feature7 = int(request.form['feature7'])

        # Prepare the input for prediction
        features = [[feature1, feature2, feature3, feature4, feature5, feature6, feature7]]
        
        # Make the prediction
        prediction = model.predict(features)

        # Return the result
        if prediction == [1]:
            result = 'Fraudulent Transaction'
        else:
            result = 'Legitimate Transaction'
        
        return render_template('index.html', prediction=result)
    
    except Exception as e:
        return f"Error: {e}"

# Run the app
if __name__ == "__main__":
    app.run(debug=True,port=5001,use_reloader=False)
