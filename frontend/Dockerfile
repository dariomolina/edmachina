FROM node:18.17.1-alpine

WORKDIR /app

COPY package.json ./

RUN npm install -g npm@10.2.0
RUN npm install

COPY . .

EXPOSE 3000

CMD ["npm", "run", "dev"]
