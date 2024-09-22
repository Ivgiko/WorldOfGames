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
    xvfb \
    && rm -rf /var/lib/apt/lists/*

# Install Google Chrome
RUN curl -sSL https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o google-chrome.deb \
    && dpkg -i google-chrome.deb \
    && apt-get install -f -y \
    && rm google-chrome.deb

# Download and install ChromeDriver that matches Chrome version
RUN wget -q https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/129.0.6668.58/linux64/chromedriver-linux64.zip \
    && unzip chromedriver-linux64.zip -d /usr/local/bin/ \
    && rm -f chromedriver-linux64.zip

# Set the working directory and copy the requirements and app code
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . /app/

# Set the display port to avoid crashes and run the tests headlessly
ENV DISPLAY=:99

# Command to run Selenium tests with XVFB
CMD ["sh", "-c", "Xvfb :99 -screen 0 1920x1080x24 & python3 /app/e2e.py"]
