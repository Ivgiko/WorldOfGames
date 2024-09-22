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
        # Navigate to the home page
        print(f"Starting test for game type {game_type} with difficulty {difficulty}...")
        print(f"Navigating to home page: {url}")
        driver.get(url)
        print(f"Current URL after navigating to home page: {driver.current_url}")

        # Wait for name form
        print("Waiting for name form (40s)...")
        WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.NAME, "name")))
        print("Name form found.")

        # Fill out the name form
        print("Filling out name form with 'Test Player'...")
        name_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "name")))
        name_field.clear()
        name_field.send_keys("Test Player")
        print("Name form filled out.")
        driver.save_screenshot(f"filled_name_form_game_type_{game_type}.png")

        # Submit the name form
        print("Submitting name form...")
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='submit']")))
        submit_button.click()
        print(f"Current URL after submitting name form: {driver.current_url}")

        # Wait for game selection form
        print("Waiting for game selection form (40s)...")
        game_field = WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.NAME, "game")))
        print(f"Current URL: {driver.current_url}")

        # Click the dropdown before sending keys
        print(f"Clicking the game dropdown to ensure it's active.")
        game_field.click()

        # Select the game and difficulty
        try:
            print(f"Selecting game type: {game_type}")
            game_field.clear()
            game_field.send_keys(str(game_type))
            driver.save_screenshot(f"selected_game_type_{game_type}.png")
        except Exception as e:
            print(f"Failed to send keys to game dropdown, trying JavaScript. Error: {e}")
            driver.execute_script(f"document.getElementById('game').value = '{game_type}';")

        print(f"Selecting difficulty: {difficulty}")
        difficulty_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "difficulty")))
        difficulty_field.clear()
        difficulty_field.send_keys(str(difficulty))
        driver.save_screenshot(f"selected_difficulty_{difficulty}.png")

        # Double-check the values in the fields
        selected_game_type = driver.execute_script("return document.getElementById('game').value;")
        selected_difficulty = driver.execute_script("return document.getElementById('difficulty').value;")
        print(f"Double-check: Selected game type: {selected_game_type}")
        print(f"Double-check: Selected difficulty: {selected_difficulty}")

        # Take a screenshot before submitting
        driver.save_screenshot(f"game_type_{game_type}_before_submit.png")

        # Submit the game selection form
        print("Submitting game selection form...")
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='submit']")))
        submit_button.click()
        print(f"Current URL after submitting game selection: {driver.current_url}")

        # Check the page source for the Memory Game
        if game_type == 1:
            WebDriverWait(driver, 40).until(EC.url_contains('/memory'))
            print("Memory Game started successfully.")
            sequence_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, 'p'))
            )
            print(f"Memory game sequence: {sequence_element.text}")
            driver.save_screenshot(f"memory_game_started.png")
        elif game_type == 2:
            WebDriverWait(driver, 40).until(EC.url_contains('/guess'))
            print("Guess Game started successfully.")
            driver.save_screenshot(f"guess_game_started.png")
        elif game_type == 3:
            WebDriverWait(driver, 40).until(EC.url_contains('/roulette'))
            print("Roulette Game started successfully.")
            driver.save_screenshot(f"roulette_game_started.png")

        return True

    except Exception as e:
        print(f"Failed to load game or start the game for game type {game_type}. Error: {e}")
        driver.save_screenshot(f"game_type_{game_type}_failed.png")
        print(f"Page source at failure:\n{driver.page_source}")
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
