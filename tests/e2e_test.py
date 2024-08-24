import requests
import sys

def test_scores_service() -> bool:
    app_url = "http://localhost:8777/score"
    try:
        response = requests.get(app_url)
        response.raise_for_status()  # Check if the request was successful

        # Debug output to understand what is being returned
        print(f"Response text: {response.text}")

        # Check the score in the response
        score = int(response.text.split("<div id=\"score\">")[1].split("</div>")[0])
        assert 0 <= score <= 1000  # Allow 0 as a valid score
    except Exception as e:
        print(f"An error occurred: {e}")
        assert False
