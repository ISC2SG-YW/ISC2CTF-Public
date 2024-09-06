# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port the app runs on
EXPOSE 3000

# Set the environment variables to specify the Flask app and environment
ENV FLASK_APP=main.py
ENV FLASK_ENV=development
ENV FLAG="ISC2CTF{848@_HA735_GR4pH_7h30rY_:c}"
# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=3000"]
