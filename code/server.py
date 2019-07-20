from flask import Flask, request, jsonify
from flask_cors import CORS

from prediction import predict

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def do_predict():
    speed = request.json['speed']
    age = request.json['age']
    miles = request.json['miles']

    predicted_category, probabilities, classes = predict(speed, age, miles)
    # print ('predicted_category:', predicted_category)
    # print ('prediction:', prediction)

    response = {
        'category': predicted_category,
        'prediction': probabilities,
        'classes': classes
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8889)

