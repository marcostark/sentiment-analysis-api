# Sentiment Analysis API

### Api for sentiment analysis using flask

- Create image:
    `docker-compose build`
- Containers running
    `docker-compose up -d`

- Testing
    `curl -X POST -H "Content-Type: application/json" \
     -d '{"text": "Text Here"}' \
     http://localhost:5000/predict`
     
### If you wish you can run the application in a virtual env

- `export FLASK_APP=app.py`
- `flask run`