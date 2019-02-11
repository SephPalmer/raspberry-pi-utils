# Use an official Python runtime as a parent image
FROM resin/rpi-raspbian:latest

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Update apt	
RUN apt-get update && \
    apt-get -qy install curl \
                ca-certificates

# Install any needed packages specified in requirements.txt
RUN apt-get install python-pip

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]

