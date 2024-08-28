# main.py

import os
from app import create_app
from app.db_init import init_db

# Initialize the database before starting the app
if not os.getenv("TEST_ENV"):
    init_db()

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8777)
