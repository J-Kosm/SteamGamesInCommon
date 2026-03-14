# Build Vue
FROM node:20 AS frontend-build

# Define /app as the working directory in the container
WORKDIR /app

# Copy package.json and similarly named files like package-lock.json to the working directory
COPY ../frontend/package*.json ./

RUN apt-get update && apt-get install -y iputils-ping

# Install dependencies, including Vite
RUN npm install
RUN npm run build

# NGINX
FROM nginx:latest

COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy built Vue files
COPY --from=frontend-build /app/dist /usr/share/nginx/html