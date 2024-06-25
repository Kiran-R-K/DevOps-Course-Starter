FROM python:3

RUN apt-get update
RUN apt-get install -y curl

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH=$PATH:/root/.local/bin/

COPY . /app
WORKDIR /app

RUN poetry install

ENTRYPOINT  poetry run flask run

EXPOSE 5000