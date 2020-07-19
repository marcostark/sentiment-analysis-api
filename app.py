from flask import Flask, request, jsonify
import os
import pickle

app = Flask(__name__)


@app.route('/')
def initial():
    return "Machine Learning API -> ON!", 200


@app.route('/predict', methods=['POST'])
def predict():
    """Performs its prediction and returns the answer to the user."""
    data = request.get_json(force=True)
    return jsonify(data)


def load_model():
    model = pickle.load(open('utils/model.pkl', 'rb'))
    return model


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
