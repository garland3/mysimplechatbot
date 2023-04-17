# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# Expose the port that the app will listen on
EXPOSE 80

WORKDIR /app/src

# Start the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
