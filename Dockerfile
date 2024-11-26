FROM python:alpine

COPY ./requirements.txt /tmp

WORKDIR /tmp

RUN pip install -r requirements.txt
