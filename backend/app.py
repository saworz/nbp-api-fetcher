import logging

from src import config, app
from apscheduler.schedulers.background import BackgroundScheduler
from src.utils.fetch_job import fetch_nbp_api

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

scheduler = BackgroundScheduler()
job = scheduler.add_job(fetch_nbp_api, trigger="cron",
                        day="*", hour="00", minute="00", max_instances=1)

if __name__ == "__main__":
    """Main execution script"""
    fetch_nbp_api()
    scheduler.start()
    app.run(
        debug=config.DEBUG,
        use_reloader=config.USE_RELOADER,
        host=config.HOST,
        port=config.PORT
    )
