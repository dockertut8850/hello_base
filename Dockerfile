FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3-flask python3-pytest

RUN mkdir /app

COPY server.py /app/server.py
COPY test_server.py /app/test_server.py
ADD templates /app/templates

EXPOSE 5000

WORKDIR /app

CMD ["python3", "server.py"]