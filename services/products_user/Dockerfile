FROM python:3.9.12

ENV PYTHONUNBUFFERED 1

RUN mkdir /user_app

WORKDIR /user_app

COPY . .

RUN pip install -r requirements.txt
