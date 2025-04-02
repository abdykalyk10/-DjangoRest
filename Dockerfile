FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONHUNBUFFERED 1

WORKDIR /app
COPY requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY . .