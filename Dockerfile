FROM gcr.io/google_appengine/python
#FROM python:3.7-alpine3.9

# if built with --build-arg pipenv_dev=1, pipenv install will include dev-packages
ARG pipenv_dev
ENV PIPENV_DEV=$pipenv_dev

RUN pip3 install --upgrade pip
RUN pip3 install pipenv

ADD . /app

WORKDIR /app

RUN pipenv install --deploy

RUN rm -rf staticfiles
RUN pipenv run python manage.py collectstatic

RUN chmod +x run.sh
ENTRYPOINT ["./run.sh"]
