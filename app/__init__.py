# app/__init__.py

import os
import logging
from flask import Flask

def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    app.logger.setLevel(logging.DEBUG)

    with app.app_context():
        from . import routes

    return app
