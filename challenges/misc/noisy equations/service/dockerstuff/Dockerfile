# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose port 5000 to the outside world
EXPOSE 5000

# Define environment variable to tell Flask it's running inside a Docker container
ENV FLASK_ENV=production
ENV FLASK_APP=app.py

# Run the Flask app
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
