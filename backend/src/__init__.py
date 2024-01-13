import logging
from flask import Flask
from flask_cors import CORS
from .config.config import Config
from apscheduler.schedulers.background import BackgroundScheduler
from .utils.fetch_job import fetch_nbp_api

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

config = Config().dev_config

scheduler = BackgroundScheduler()
job = scheduler.add_job(fetch_nbp_api, trigger="cron",
                        day="*", hour="00", minute="00", max_instances=1)

from .routes.routes import routes
app.register_blueprint(routes)
