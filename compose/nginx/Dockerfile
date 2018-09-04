FROM nginx:latest

USER root

RUN apt-get update
RUN apt-get install -y build-essential
RUN apt-get -y install curl

RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -
RUN apt-get -y install nodejs

RUN npm install -g webpack webpack-dev-server webpack-cli


WORKDIR /app
ADD . /app

RUN npm install

RUN webpack --mode development

COPY static /usr/share/nginx/html
