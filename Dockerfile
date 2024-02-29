# Use a Node.js Alpine-based image for the development stage
FROM node:18-alpine

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy application dependency manifests to the container image
COPY package*.json ./

# Install application dependencies using `npm install`
RUN npm install

# Copy the rest of the application code to the container
COPY . .

# Build the application (if needed)
RUN npm run build

# Copie o script de entrada (entrypoint) para dentro do contêiner
COPY entrypoint.sh /app/entrypoint.sh

# Torne o script de entrada executável
RUN chmod +x /app/entrypoint.sh

# Defina o script de entrada como o ponto de entrada do contêiner
ENTRYPOINT ["/bin/sh", "-c","/app/entrypoint.sh"]

# Define the command to start your application in development mode
# ENTRYPOINT ["/bin/sh", "-c", "npm run start:dev"]
# ENTRYPOINT ["entrypoint.sh"]