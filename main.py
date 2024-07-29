from app import create_app

app = create_app()

if __name__ == "__main__":
    app.logger.info("Starting Flask app on port 8777")
    app.run(debug=True, host='0.0.0.0', port=8777)
