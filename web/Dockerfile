FROM python:3.6
#ADD .. /src
#WORKDIR /src
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
CMD python3 app.py
COPY . .