from . import app, config, scheduler


def flask_server() -> None:
    app.run(
        debug=config.debug,
        use_reloader=config.use_reloader,
        host=config.host,
        port=config.port,
        threaded=config.threaded
    )


async def async_scheduler() -> None:
    scheduler.start()
