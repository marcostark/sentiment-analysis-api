# Flask Boilerplate for Machine Learning

Flask template for machine learning project microservice

- Create container
    `docker-compose up -d`

- Testing
    `curl -X POST -H "Content-Type: application/json" \
     -d '{"text": "Text Here"}' \
     http://127.0.0.1:5000/predict`