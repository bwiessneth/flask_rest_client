from config import Config
from app import create_app

app = create_app()

# If app.py is run directly start in debug mode
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=Config.FLASK_RUN_PORT, debug=True)
