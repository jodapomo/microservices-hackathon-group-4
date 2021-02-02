FROM node:12.18-alpine

RUN mkdir -p /usr/app

WORKDIR /usr/app

COPY package.json .

COPY package-lock.json .

RUN npm install

COPY server.js .

COPY env.js .

ENTRYPOINT node server.js
