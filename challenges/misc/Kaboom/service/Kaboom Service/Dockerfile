# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container
COPY . .

# Install socat
RUN apt-get update && apt-get install -y socat

# Expose the port your service will run on
EXPOSE 323

ENV FLAG="ISC2CTF{B4B4_lOVe5_dPdPdpdpDpDPDPdp}"

# Run socat to handle the TCP connection and forward it to the Python script
CMD socat TCP-LISTEN:323,fork EXEC:"python3 main.py"
