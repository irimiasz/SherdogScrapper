FROM python:3.11.0
RUN pip install pipenv
WORKDIR /code
COPY Pipfile /code/Pipfile
COPY Pipfile.lock /code/Pipfile.lock
RUN pipenv install
COPY ./src /code/src
