from flask import Flask, request, Response, jsonify

from utils import load_model, process_data, predict

model = load_model()

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome!'

@app.route('/recommend/', methods=['POST'])
def recommend():
    request_body = request.get_json()
    print(request_body)

    model_features = process_data(request_body)
    print(model_features)

    prediction = predict(model_features, model)
    print(prediction)

    return jsonify({'recommendation': prediction})


if __name__ == '__main__':
    model = load_model()
    app.run(debug=True)