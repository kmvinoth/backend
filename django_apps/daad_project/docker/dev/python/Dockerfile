# pull official base image
FROM python:3.6.10-slim-stretch

# copy entrypoint file
COPY ./docker/dev/python/entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

# set work directory
WORKDIR /app

# install dependencies
COPY ./app/requirements /app/requirements

RUN pip install --no-cache-dir -r requirements/dev.txt

# copy project
COPY ./app /app


ENTRYPOINT ["/entrypoint.sh"]