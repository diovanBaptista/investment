FROM node:18

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build

EXPOSE 3000

# CMD [ "npm", "run", "start:dev" ]

# Copiando o entrypoint.sh
COPY entrypoint.sh /usr/local/bin/

RUN chmod +x /usr/local/bin/entrypoint.sh

# Especificando o entrypoint.sh como o ponto de entrada
ENTRYPOINT ["/bin/bash", "-c", "/usr/local/bin/entrypoint.sh"]