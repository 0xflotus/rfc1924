# This Dockerfile is only for test purposes.

FROM python:3.9-alpine
LABEL maintainer "0xflotus"

RUN apk add --virtual build-deps --no-cache gcc musl-dev 

RUN mkdir /app
COPY . /app
WORKDIR /app

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install rfc1924

RUN python3 ./rfc1924/test_rfc1924.py
