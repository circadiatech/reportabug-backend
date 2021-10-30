# pull official base image
FROM python:3.8.9

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && apt-get install -y netcat

# install dependencies
RUN pip install pipenv
COPY Pipfile Pipfile.lock /usr/src/app/
RUN pipenv install --system --dev

# copy project
COPY . /usr/src/app/
