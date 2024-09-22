# Use a Python image
FROM python:3.11-slim-buster

# Set the working directory inside the container
WORKDIR /app

# Copy the contents of the current directory to /app in the container
COPY . /app

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app will run on
EXPOSE 5002

# Run the application
CMD ["python", "GuessGame.py"]
