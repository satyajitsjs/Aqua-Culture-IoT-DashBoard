# Use an official Python runtime as a parent image
FROM ubuntu:latest

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

RUN apt-get update && \
    apt-get install -y \
    python3 \
    python3-venv \
    python3-pip 

# Install GDAL dependencies
RUN apt-get update
RUN apt-get install -y mesa-utils
RUN apt-get install -y libegl-mesa0
RUN apt-get install -y gdal-bin libgdal-dev
RUN rm -rf /var/lib/apt/lists/*

# Ensure pip installs packages into Python 3
RUN ln -sf /usr/bin/python3 /usr/bin/python && \
    ln -sf /usr/bin/pip3 /usr/bin/pip


RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"


# Copy the requirements file into the container at /app
COPY linux-requirement.txt /app/

# Install any needed packages specified in linux-requirement.txt
RUN pip install --no-cache-dir -r linux-requirement.txt

# Copy the rest of the application code into the container at /app
COPY . /app/

# Expose the port the app runs on
EXPOSE 80

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
