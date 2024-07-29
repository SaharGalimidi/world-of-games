import requests
import sys
import re

def test_scores_service(app_url: str) -> bool:
    try:
        response = requests.get(app_url)
        response.raise_for_status()  # Check if the request was successful

        # Extract score using regex
        match = re.search(r'<div id="score">(\d+)</div>', response.text)
        if match:
            score = int(match.group(1))
            return 1 <= score <= 1000
        else:
            print("Score not found in the response")
            return False
    except (requests.RequestException, ValueError) as e:
        print(f"An error occurred: {e}")
        return False

def main_function():
    app_url = "http://localhost:8777/score"  # URL to fetch the score
    print(f"URL to test: {app_url}")
    test_result = test_scores_service(app_url)
    if test_result:
        print("Test pass")
        sys.exit(0)
    else:
        print("Test fail")
        sys.exit(-1)

if __name__ == "__main__":
    main_function()
