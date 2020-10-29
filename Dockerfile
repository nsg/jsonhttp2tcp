FROM python:3-slim

ADD src /app

WORKDIR /app
RUN pip install -r requirements.txt
RUN pip install .

RUN adduser --uid 1001 --gecos false --disabled-password --disabled-login app
USER app
ENV INDOCKER=1

ENTRYPOINT ["/usr/local/bin/service"]
