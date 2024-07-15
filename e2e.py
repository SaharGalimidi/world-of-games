# e2e.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import sys
import time
import requests

def wait_for_service(url, timeout=60):
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return True
        except requests.exceptions.ConnectionError:
            time.sleep(1)
    return False

def test_scores_service(url: str) -> bool:
    options = Options()
    options.headless = True
    service = Service(executable_path='/usr/local/bin/chromedriver')  # Adjust the path as necessary
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(url)
        time.sleep(2)  # wait for the page to load
        score_element = driver.find_element(By.ID, "score")
        score = int(score_element.text)
        return 1 <= score <= 1000
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    finally:
        driver.quit()

def main_function():
    url = "http://localhost:5000/score"
    if wait_for_service(url):
        if test_scores_service(url):
            sys.exit(0)
        else:
            sys.exit(-1)
    else:
        print("Service did not start in time")
        sys.exit(-1)

if __name__ == "__main__":
    main_function()
