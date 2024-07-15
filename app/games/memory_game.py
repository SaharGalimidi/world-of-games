import random
from typing import List
import logging

logger = logging.getLogger(__name__)

def generate_sequence(difficulty: int) -> List[int]:
    sequence = [random.randint(1, 101) for _ in range(difficulty)]
    logger.debug(f'Generated sequence: {sequence}')
    return sequence

def is_list_equal(list1: List[int], list2: List[int]) -> bool:
    equal = list1 == list2
    logger.debug(f'Comparing lists {list1} and {list2}: {equal}')
    return equal
