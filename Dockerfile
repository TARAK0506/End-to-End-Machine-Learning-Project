# FROM baseImage
# COPY source dest
# WORKDIR /the/workdir/path
# RUN command
# EXPOSE 80
# CMD ["executable"]


# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY requirements.txt ./
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
# RUN ls -l /app/Notebook/


# Make port 80 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME=World

# Run app.py when the container launches
CMD ["python", "app.py"]

# # Build the image
# docker build -t my-python-app .

# # Run the image
# docker run -p 4000:80 my-python-app

# # Stop the container
# docker stop <container_id>

# # Remove the container
# docker rm <container_id>

# # Remove the image
# docker rmi my-python-app

# # List all containers
# docker ps -a

# # List all images
# docker images

# # List all networks
# docker network ls

# # List all volumes
# docker volume ls
