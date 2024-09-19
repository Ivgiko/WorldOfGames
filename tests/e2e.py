from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options
chrome_options = Options()
chrome_options.binary_location = "/usr/bin/google-chrome"
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
chrome_options.add_argument("--no-sandbox")  # Disable sandboxing (necessary in Docker)
chrome_options.add_argument("--disable-dev-shm-usage")  # Disable /dev/shm usage
chrome_options.add_argument("--remote-debugging-port=9222")  # Enable remote debugging
chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration

# Create a Service object to specify the path to ChromeDriver
service = Service(ChromeDriverManager().install())

# Initialize the WebDriver with the specified options and service
driver = webdriver.Chrome(service=service, options=chrome_options)

def test_scores_service(url):
    try:
        dr = webdriver.Chrome(service=service, options=chrome_options)
        dr.get(url)
        score = dr.find_element(by="id", value="score").text
        if 1 <= int(score) <= 1000:
            return True
        else:
            return False
    except AssertionError as e:
        return False

def main():
    url = "http://web:5000"
    if test_scores_service(url):
        print("cool!")
        return 0
    else:
        print("damn!")
        return -1

main()
