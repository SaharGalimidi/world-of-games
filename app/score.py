import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import logging
from libs.postgres.db import get_db
from libs.postgres.models import Score

logger = logging.getLogger(__name__)

BAD_RETURN_CODE = -1

def get_score(player_name: str) -> int:
    try:
        db = next(get_db())
        score_record = db.query(Score).filter(Score.player_name == player_name).all()
        if score_record:
            total_score = 0
            for record in score_record:
                total_score += record.score
            logger.debug(f"Current score for {player_name}: {total_score}")
            return total_score
        else:
            logger.debug(f"No score record found for {player_name}. Returning 0.")
            return 0
    except Exception as e:
        logger.error(f"Error retrieving score for {player_name}: {e}")
        return BAD_RETURN_CODE
    
def add_score(player_name: str, game_name: str, difficulty: int) -> None:
    points_of_winning = (difficulty * 3) + 5
    try:
        db = next(get_db())
        new_score = Score(player_name=player_name, game_name=game_name, score=points_of_winning)
        db.add(new_score)
        db.commit()
        logger.debug(f"Created new score record for {player_name}: {new_score.score}")
        return None
    except Exception as e:
        db.rollback()
        logger.error(f"Error adding score for {player_name}: {e}")
        return None


    



