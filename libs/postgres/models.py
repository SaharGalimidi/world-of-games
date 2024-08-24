from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Score(Base):
    __tablename__ = 'scores'

    id = Column(Integer, primary_key=True)
    player_name = Column(String, nullable=False)
    game_name = Column(String, nullable=False)
    score = Column(Integer, nullable=False)
    date = Column(DateTime, default=datetime.now(datetime.now().astimezone().tzinfo))

    def __repr__(self):
        return f"<Score(player_name='{self.player_name}', game_name='{self.game_name}', score={self.score})>"