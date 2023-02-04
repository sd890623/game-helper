FROM python:3.8-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./src ./src
COPY requirements.txt ./requirements.txt

# Install the required packages
# RUN pip install --no-cache-dir -r requirements.txt

# Define environment variable
ENV PYTHONUNBUFFERED 1

# Run the command to start the application
CMD ["python", "./src/playground.py"]