import logging
from flask import Flask
from flask_cors import CORS
from .config import Config, FetchConfig
from apscheduler.schedulers.background import BackgroundScheduler
from .services.cyclic_job import fetch_nbp_api
from .routes.routes import routes
from datetime import datetime

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

config = Config().dev_config
fetch_config = FetchConfig()

scheduler = BackgroundScheduler()
job = scheduler.add_job(fetch_nbp_api, next_run_time=datetime.now(), trigger="cron",
                        day="*", hour="00", minute="00", max_instances=1)

app.register_blueprint(routes)
