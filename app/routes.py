from app import app
from flask import render_template

# Index endpoint
@app.route("/")
def index():
	message = "Hello from flask_rest_client"
	return render_template('index.html', message=message)
