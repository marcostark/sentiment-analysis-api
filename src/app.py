from flask import Flask, request, jsonify
import os
import pickle

from nltk.stem.snowball import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from unpickler import CustomUnpickler

app = Flask(__name__)


# was used as a tokenizer when creating the TFIDF object
def tokenizer_porter(text):
    """
    Split the comment text into a single word and extract the stem,
    :param text:
    :return:
    """
    porter = PorterStemmer()
    return [porter.stem(word) for word in text.split()]


with open('vectorizer.pkl', 'rb') as f:
    unpickler = CustomUnpickler(f)
    vectorizer = TfidfVectorizer()
    vectorizer = unpickler.load()

with open('sentiment_analysis_model.pkl', 'rb') as f:
    unpickler = CustomUnpickler(f)
    model = unpickler.load()


@app.route('/')
def initial():
    return "Machine Learning API -> ON!", 200


@app.route('/predict', methods=['POST'])
def predict():
    """Performs its prediction and returns the answer to the user."""
    data = request.get_json(force=True)
    return jsonify(data)


def load_model():
    model = pickle.load(open('src/utils/model.pkl', 'rb'))
    return model


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
