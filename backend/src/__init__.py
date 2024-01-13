from flask import Flask
from flask_cors import CORS
from .config.config import Config

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

config = Config().dev_config

from .routes.routes import routes
app.register_blueprint(routes)
