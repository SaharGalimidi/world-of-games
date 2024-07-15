import random
import requests
from typing import Tuple
import logging

logger = logging.getLogger(__name__)

def get_money_interval(difficulty: int) -> Tuple[float, float]:
    response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
    rate = response.json()["rates"]["ILS"]
    #t = random.randint(1, 100)
    lower = (5 - difficulty)
    upper = (5 + difficulty)
    interval = (lower * rate, upper * rate)
    logger.debug(f'Generated interval for difficulty {difficulty}: {interval}')
    return interval
