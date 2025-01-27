# Use an official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the Python script to the container
COPY app.py /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt 

COPY . .

# Command to run the Python script
CMD ["python", "app.py"]

EXPOSE 8000