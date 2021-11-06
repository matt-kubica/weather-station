FROM node:16.12.0

ENV NPM_CONFIG_PREFIX=/home/node/.npm-global
ENV PATH /home/node/.npm-global/bin:$PATH
RUN npm i --unsafe-perm -g npm@latest expo-cli@latest

RUN mkdir /opt/mobile && chown node:node /opt/mobile
WORKDIR /opt/mobile
ENV PATH /opt/mobile/.bin:$PATH
COPY ./package.json package-lock.json ./
RUN npm install

EXPOSE 19000 19001 19002