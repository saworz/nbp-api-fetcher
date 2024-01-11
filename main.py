from server import app
from apscheduler.schedulers.background import BackgroundScheduler
from nbp_api import fetch_nbp_api

scheduler = BackgroundScheduler()
job = scheduler.add_job(fetch_nbp_api, trigger="cron",
                        day="*", hour="00", minute="00", max_instances=1)

if __name__ == "__main__":
    fetch_nbp_api()
    scheduler.start()
    app.run(debug=True, use_reloader=False)
