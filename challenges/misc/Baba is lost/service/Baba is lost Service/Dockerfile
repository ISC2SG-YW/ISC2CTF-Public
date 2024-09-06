# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container
COPY . .

# Install socat
RUN apt-get update && apt-get install -y socat

# Expose the port your service will run on
EXPOSE 12345

ENV FLAG="ISC2CTF{Ba8@_l0VeS_b1N4ry_5earcH}"

# Run socat to handle the TCP connection and forward it to the Python script
CMD socat TCP-LISTEN:12345,fork EXEC:"python3 main.py"
