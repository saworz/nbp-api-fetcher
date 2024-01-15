from src import config, app, scheduler

if __name__ == "__main__":

    """Main execution script"""
    scheduler.start()
    app.run(
        debug=config.debug,
        use_reloader=config.use_reloader,
        host=config.host,
        port=config.port
    )
