# Sentiment Analysis API

### Api for sentiment analysis using flask

- Create container
    `docker-compose up -d`

- Testing
    `curl -X POST -H "Content-Type: application/json" \
     -d '{"text": "Text Here"}' \
     http://127.0.0.1:5000/predict`