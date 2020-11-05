FROM python:3.6

RUN pip install flask

COPY . /opt/

EXPOSE 8080

WORKDIR /opt

ENV VERSION=v2
ENV ROCKET_SIZE=average

ENTRYPOINT ["python3", "app.py"]