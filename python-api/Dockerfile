FROM python:3.7.10

ENV PYTHONUNBUFFERED 1

RUN mkdir /auth_project

WORKDIR /auth_project

COPY . /auth_project/

RUN pip install -r requirements.txt
