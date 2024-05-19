# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Copy the keep-alive script
COPY keep_alive.sh .

# Make the script executable
RUN chmod +x keep_alive.sh

# Start the keep-alive script
CMD ["./keep_alive.sh"]
