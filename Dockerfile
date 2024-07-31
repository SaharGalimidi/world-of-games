# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Scores.txt file into the container
COPY Scores.txt /Scores.txt

EXPOSE 8777
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=main.py

# Run the application
CMD ["flask", "run", "--host=0.0.0.0", "--port=8777"]
