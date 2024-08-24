import os
from alembic import command
from alembic.config import Config
import logging

def init_db():
    alembic_cfg = Config(os.path.join(os.path.dirname(__file__), '..', 'libs/postgres/alembic.ini'))
    command.upgrade(alembic_cfg, "head")
    logging.info("Database initialized successfully.")
