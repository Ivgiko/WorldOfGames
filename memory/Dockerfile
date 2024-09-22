# Use a Python image
FROM python:3.9-slim

# Install required dependencies
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the game files
COPY . /app

# Expose the port for Flask app
EXPOSE 5001

# Run the Memory Game Flask app
CMD ["python", "MemoryGame.py"]
