import os
import logging

logger = logging.getLogger(__name__)

SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = -1

def get_score() -> int:
    try:
        with open(SCORES_FILE_NAME, "r") as f:
            score = int(f.read())
            logger.debug(f'Current score: {score}')
            return score
    except Exception as e:
        logger.error(f'Error reading score: {e}')
        return BAD_RETURN_CODE

def add_score(difficulty: int) -> None:
    points_of_winning = (difficulty * 3) + 5
    try:
        current_score = get_score()
        if current_score == BAD_RETURN_CODE:
            current_score = 0
        new_score = current_score + points_of_winning
        with open(SCORES_FILE_NAME, "w") as f:
            f.write(str(new_score))
        logger.debug(f'Added score {points_of_winning} for difficulty {difficulty}, new score: {new_score}')
    except Exception as e:
        logger.error(f'Error adding score: {e}')
