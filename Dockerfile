# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port that the Flask app will run on
EXPOSE 8080

# Define the command to run the application
# Use Gunicorn as a production-ready WSGI server
# Install gunicorn first: pip install gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]