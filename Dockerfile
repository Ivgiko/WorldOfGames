FROM python:3.9-buster

WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app/

# Expose the Flask app port
EXPOSE 5000

# Run Alembic migrations and start the Flask app automatically
CMD alembic revision --autogenerate -m "Create users_scores table" && alembic upgrade head && python MainGame.py
