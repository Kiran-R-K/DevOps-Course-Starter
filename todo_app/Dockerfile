FROM python:3

RUN apt-get update
RUN apt-get install -y curl

RUN curl -sSL https://install.python-poetry.org | python3 -

WORKDIR /todo_app
COPY ./todo_app ./todo_app

RUN poetry install

RUN poetry install pytest

RUN poetry run flask run