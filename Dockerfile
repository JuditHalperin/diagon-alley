# syntax=docker/dockerfile:1

# Use the official Python image
FROM python:3.8-slim-buster

# Create a working directory as the default location for all subsequent commands
WORKDIR /app

# Get the requirements into the image working directory
COPY requirements.txt .

# Ensures all dependencies are installed
RUN pip3 install -r requirements.txt

# Add all Python scripts to the image working directory
COPY ./*.py .

# Run the following command when the image is executed inside a container (-u = show prints in docker logs)
CMD ["python", "-u", "./main.py"]