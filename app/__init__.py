#!/usr/bin/env python3.6
import os
from flask import Flask
from flask_middleware import PrefixMiddleware
from config import Config

app = Flask(__name__)

def create_app(config_class=Config):
	# app = Flask(__name__)
	app.config.from_object(config_class)

	# Set the prefix for serving the app. Uncomment if '/' shall be used
	app.wsgi_app = PrefixMiddleware(app.wsgi_app, prefix='/flask_rest_client')

	return app

from app import routes
