FROM python:3.8

ADD requirements.txt /requirements.txt

RUN pip install -r requirements.txt

ADD . /code
WORKDIR /code

CMD ["python", "main.py"]
