from flask import Flask, request, jsonify
from flask_cors import CORS

from prediction import predict

app = Flask(__name__)
CORS(app)

import logging

logging.basicConfig(filename='req.log')

data_logger = logging.getLogger('DataLogger')
data_logger.setLevel(logging.INFO)

file_handler = logging.FileHandler('data.log', )

data_logger.addHandler(file_handler)

@app.route("/ping")
def ping():
    return "pong"

@app.route('/predict', methods=['GET', 'POST'])
def do_predict():
    speed = request.json['speed']
    age = request.json['age']
    miles = request.json['miles']

    predicted_category, probabilities = predict(speed, age, miles)

    response = {
        'category': predicted_category,
        'prediction': probabilities,
    }

    dataset = {
        'out': response,
        'in': {
            'speed': speed, 'age': age, 'miles': miles
        }
    }

    data_logger.info(dataset)
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)

