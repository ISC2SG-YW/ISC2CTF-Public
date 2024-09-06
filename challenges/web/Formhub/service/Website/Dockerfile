# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory
WORKDIR /app
RUN mkdir -p /tables
# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port the app runs on
EXPOSE 5000


# Set the environment variables to specify the Flask app and environment
ENV SECRET_KEY="jC2GGWg1CFrDJ#Xgj*bCP#lDoP#rY"
ENV FLASK_APP=main.py
ENV FLASK_ENV=development
ENV FLAG="ISC2CTF{b@ba_l0VEs_f0rM_ON_X\$\$_4Nd_5Q11}"
# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]
