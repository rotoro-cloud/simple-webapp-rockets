FROM python:3.6-alpine

RUN pip install flask

COPY . /opt/

EXPOSE 8080

WORKDIR /opt

ENV VERSION=v1
ENV ROCKET_SIZE=small

ENTRYPOINT ["python3", "app.py"]