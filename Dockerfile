FROM python:3.9

COPY . /code

WORKDIR /code

RUN apt-get update &&\
    apt-get install -y binutils libproj-dev gdal-bin
RUN pip install urllib3
RUN pip install poetry
RUN poetry install
# RUN poetry run python ./manage.py migrate

CMD ['/usr/local/bin/poetry', 'run', 'python', './manage.py', 'runserver 0.0.0.0:8000']