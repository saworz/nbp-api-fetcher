from src import config, app, scheduler
from src.utils.fetch_job import fetch_nbp_api

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
