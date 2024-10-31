# Use an official Python runtime as a parent image
# very slim version of linuxOS 
FROM python:3.9-slim

# Set the working directory in the container
# creating app folder ion a linux image
WORKDIR /app

# Copy the required files to the container
# copying files from my mac to app folder in linux image
# COPY api.py /app/api.py
# COPY model.py /app/model.py
# COPY mongo.py /app/mongo.py
# COPY requirements.txt /app/requirements.txt
# Copy the application code into the container at /app
#copies all the folders in the image
COPY . .

# Install dependencies from requirements.txt
#installing required commands in already installed python enviroment in linux image
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Flask app port (if your Flask app runs on port 5000)
EXPOSE 8000

# Set the environment variable for Flask
# ENV FLASK_ENV=development

# Run the API when the container starts
#same as writing python api.py on terminal
CMD ["python3", "./api.py"]
