# Use an official Node.js runtime as a parent image
FROM node:14-slim

# Set the working directory to /app
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the entire project to work directory
COPY . .

# Build the application to the dist folder
RUN npm run production

# Install 'serve' to serve the static files
RUN npm install -g serve

# Command to serve the dist directory on port 8080
CMD ["serve", "-s", "dist", "-l", "8080"]

# Expose port 8080
EXPOSE 8080
