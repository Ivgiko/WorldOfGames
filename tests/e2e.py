import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

def test_game_access(driver, url, game_type, difficulty):
    """
    Test if a specific game can be accessed and started.
    :param game_type: 1 for Memory Game, 2 for Guess Game, 3 for Roulette.
    :param difficulty: Difficulty level for the game.
    """
    try:
        # Start the test for the game
        print(f"Starting test for game type {game_type} with difficulty {difficulty}...")
        print(f"Navigating to home page: {url}")
        driver.get(url)

        # Wait for name form
        WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.NAME, "name")))
        print("Filling out name form with 'Test Player'...")
        name_field = driver.find_element(By.NAME, "name")
        name_field.clear()
        name_field.send_keys("Test Player")

        # Submit the name form
        submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
        submit_button.click()

        # Wait for game selection form
        WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.NAME, "game")))
        print(f"Selecting game type: {game_type}")
        driver.find_element(By.NAME, "game").send_keys(str(game_type))
        print(f"Selecting difficulty: {difficulty}")
        driver.find_element(By.NAME, "difficulty").send_keys(str(difficulty))

        # Submit the game selection form
        submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
        submit_button.click()

        # Check for the correct game page
        if game_type == 1:
            WebDriverWait(driver, 40).until(EC.url_contains('/memory'))
            print("Memory Game started successfully.")
        elif game_type == 2:
            WebDriverWait(driver, 40).until(EC.url_contains('/guess'))
            print("Guess Game started successfully.")
        elif game_type == 3:
            WebDriverWait(driver, 40).until(EC.url_contains('/roulette'))
            print("Roulette Game started successfully.")

        return True

    except Exception as e:
        print(f"Failed to load game or start the game for game type {game_type}. Error: {e}")
        return False

# Main entry for testing
def main():
    url = "http://flask_app:5000/"

    # Set up Chrome options for running in headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(options=chrome_options)

    # Test Memory Game
    if not test_game_access(driver, url, game_type=1, difficulty=2):
        driver.quit()
        return -1

    # Test Guess Game
    if not test_game_access(driver, url, game_type=2, difficulty=2):
        driver.quit()
        return -1

    # Test Roulette Game
    if not test_game_access(driver, url, game_type=3, difficulty=2):
        driver.quit()
        return -1

    driver.quit()
    return 0

if __name__ == "__main__":
    result = main()
    if result == 0:
        print("All tests passed successfully.")
    else:
        print("Some tests failed.")
    exit(result)
