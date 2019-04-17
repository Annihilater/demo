FROM daocloud.io/python:3.6

WORKDIR /app

ENV REDIS_HOST='redis'
ENV FLAKS_APP='app.py'
ENV FLAKS_ENV='production'

COPY . ./

RUN pip install pipenv pip && \
    pipenv --python 3.6 && \
    pipenv sync

