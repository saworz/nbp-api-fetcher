from . import app, config, scheduler


def flask_server() -> None:
    app.run(
        debug=config.DEBUG,
        use_reloader=config.USE_RELOADER,
        host=config.HOST,
        port=config.PORT,
        threaded=True
    )


async def async_scheduler() -> None:
    scheduler.start()
