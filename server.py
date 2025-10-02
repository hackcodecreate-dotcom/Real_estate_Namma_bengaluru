# server.py

from flask import Flask, request, jsonify
import util
import logging

# Initialize Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Load model and artifacts
util.load_saved_artifacts()

@app.before_request
def log_request_info():
    """Log incoming request data for debugging"""
    logging.info(f"Received {request.method} request at {request.path} with data: {request.get_json()}")

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    """Return all known locations"""
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    """Predict home price given location, sqft, BHK, and bathrooms"""
    data = request.form if len(request.form) > 0 else request.json

    try:
        # Validate inputs
        sqft     = float(data.get('total_sqft', 0))
        location = data.get('location')
        bhk      = int(data.get('bhk', 0))
        bath     = int(data.get('bath', 0))

        if not location:
            raise ValueError("Location is required")
        if sqft <= 0 or bhk <= 0 or bath <= 0:
            raise ValueError("Square feet, BHK, and bathrooms must be positive numbers")

        # Get estimated price
        estimated_price = util.get_estimated_price(location, sqft, bhk, bath)

        response = jsonify({'estimated_price': estimated_price})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    except (ValueError, TypeError) as e:
        response = jsonify({'error': str(e)})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response, 400

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    app.run(debug=True)
