import random
import logging

logger = logging.getLogger(__name__)

def generate_number(difficulty: int) -> int:
    number = random.randint(1, difficulty)
    logger.debug(f'Generated number: {number}')
    return number

def compare_results(secret_number: int, guess: int) -> bool:
    result = secret_number == guess
    logger.debug(f'Comparing secret number {secret_number} and guess {guess}: {result}')
    return result
