#!/bin/bash

FROM python:3.7

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt --no-cache-dir

CMD ["restaurant_service.py"]
