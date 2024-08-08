# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Install NGINX
RUN apt-get update && apt-get install -y nginx

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt requirements.txt

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Copy NGINX configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expose the port NGINX will run on
EXPOSE 80

# Create a start script
RUN echo '#!/bin/bash\nservice nginx start\ngunicorn --bind 0.0.0.0:5000 app:app' > /start.sh && chmod +x /start.sh

# Start NGINX and the Flask app using Gunicorn
CMD ["/start.sh"]
