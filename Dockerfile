# Use Python base image
FROM python:3.9-slim

# Install required system packages
RUN apt-get update && apt-get install -y gcc libpq-dev

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . .
