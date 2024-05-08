FROM node:20

# Create app directory
WORKDIR /usr/src/manager/

COPY package*.json ./

RUN npm install

COPY . .   

EXPOSE 3000

CMD ["npm", "start"]

