FROM python:3.6
ADD . /src
WORKDIR /src
RUN pip3 install -r requirements.txt
CMD python3 app.py