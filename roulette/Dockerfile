# Use a Python image
FROM python:3.11-slim-buster

# Set work directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files
COPY . /app

# Expose port 5003 for the currency roulette game service
EXPOSE 5003

# Command to run the flask application
CMD ["python", "CurrencyRouletteGame.py"]
