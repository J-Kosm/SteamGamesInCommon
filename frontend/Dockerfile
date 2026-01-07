FROM node:20

# Define /app as the working directory in the container
WORKDIR /app

# Copy package.json and similarly named files like package-lock.json to the working directory
COPY package*.json ./

# Install dependencies, including Vite
RUN npm install
RUN npm install -D vite

# Copy the other application files
COPY . .

EXPOSE 5173

# Run Vite when the container starts
CMD ["npm", "run", "dev", "--", "--host"]