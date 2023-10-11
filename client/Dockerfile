FROM node:18-alpine
WORKDIR /app
COPY package.json .
RUN npm install
RUN npm install react-scripts
RUN npm install react react-dom --save
RUN export NODE_OPTIONS=--openssl-legacy-provider
COPY . .
EXPOSE 3000
CMD ["npm", "start"]