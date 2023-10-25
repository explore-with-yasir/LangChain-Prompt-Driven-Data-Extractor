from flask import Flask

# Create the Flask application
app = Flask(__name__)

# Load configuration from a config.py file (assuming it's in the same directory as main.py)
# app.config.from_object('config')

# Import and register API blueprints
from app.api.google_drive_api import google_drive_api
from app.api.similarity_search_api import similarity_search_api
app.register_blueprint(google_drive_api)
app.register_blueprint(similarity_search_api)
