FROM python:3.6


USER root

RUN apt-get update
RUN apt-get install -y build-essential
RUN apt-get -y install supervisor
RUN apt-get -y install systemd

WORKDIR /app
ADD . /app
ENV PYTHONPATH /app

RUN pip3 install pipenv
RUN pipenv install --dev --system --deploy

COPY ./compose/server/entrypoint.sh /app/entrypoint.sh
COPY ./compose/server/supervisord.conf /etc/supervisor/supervisord.conf

RUN chmod +x /app/entrypoint.sh
RUN chmod +x /etc/supervisor/supervisord.conf

RUN mkdir /var/log/parser

ENTRYPOINT ["/bin/bash", "/app/entrypoint.sh"]
