#!/bin/bash

FROM python:3.8

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt --no-cache-dir

CMD ["login_service.py"]
