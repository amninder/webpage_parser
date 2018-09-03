FROM python:3.6


USER root

RUN apt-get update
RUN apt-get install -y build-essential
RUN apt-get -y install supervisor
RUN apt-get -y install systemd
RUN apt-get -y install nginx
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -
RUN apt-get -y install nodejs

RUN npm install -g webpack webpack-dev-server webpack-cli

WORKDIR /app
ADD . /app
ENV PYTHONPATH /app

RUN pip3 install pipenv
RUN pipenv install --dev --system --deploy

COPY ./compose/entrypoint.sh /app/entrypoint.sh
COPY ./compose/supervisord.conf /etc/supervisor/supervisord.conf

RUN chmod +x /app/entrypoint.sh
RUN chmod +x /etc/supervisor/supervisord.conf

RUN mkdir /var/log/urlshortner

EXPOSE 8000

ENTRYPOINT ["/bin/bash", "/app/entrypoint.sh"]
