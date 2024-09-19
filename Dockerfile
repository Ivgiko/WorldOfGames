# Use a Python image
FROM python:3.11-slim-buster

# Install required dependencies
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    libxi6 \
    libgconf-2-4 \
    libnss3 \
    libx11-xcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libatk1.0-0 \
    libcups2 \
    libgdk-pixbuf2.0-0 \
    libxkbcommon0 \
    libxshmfence1 \
    fonts-liberation \
    libappindicator3-1 \
    lsb-release \
    curl \
    libasound2 \
    libdrm2 \
    libgbm1 \
    libvulkan1 \
    xdg-utils \
    && rm -rf /var/lib/apt/lists/*

# Install Google Chrome
RUN curl -sSL https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o google-chrome.deb \
    && dpkg -i google-chrome.deb \
    && apt-get install -f -y \
    && rm google-chrome.deb

# Download and install ChromeDriver
RUN wget -q https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip \
    && unzip chromedriver_linux64.zip -d /usr/local/bin/ \
    && rm -f chromedriver_linux64.zip

# Install Python dependencies
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . /app/

# Expose the port for Flask app
EXPOSE 5000

# Run the Flask app
CMD ["python3", "MainScores.py"]
