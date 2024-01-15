from src import config, app, scheduler

if __name__ == "__main__":

    """Main execution script"""
    scheduler.start()
    app.run(
        debug=config.DEBUG,
        use_reloader=config.USE_RELOADER,
        host=config.HOST,
        port=config.PORT
    )
