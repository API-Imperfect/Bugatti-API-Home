FROM python:3.9-alpine
# set our working directory inside the container (when it's finally created from this image)
# depending on your environment you may need to
# RUN mkdir -p /app
WORKDIR /app
# set environment variables
# Prevents Python from writing .pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1

# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
  && apk add --virtual build-deps gcc python3-dev musl-dev \
  && apk add postgresql-dev gcc python3-dev musl-dev \
  && apk del build-deps \
  && apk --no-cache add musl-dev linux-headers g++

RUN apk add --no-cache \
        libressl-dev \
        musl-dev \
        libffi-dev && \
    pip install --no-cache-dir cryptography==2.1.4 && \
    apk del \
        libressl-dev \
        musl-dev \
        libffi-dev
        
# upgrade pip version
RUN pip install --upgrade pip

# copy requirements to the image
COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

# Copy over the project
COPY . /app