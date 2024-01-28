from src.tasks import flask_server, async_scheduler
import threading
import asyncio


if __name__ == "__main__":
    """Main execution script"""
    flask_thread = threading.Thread(target=flask_server)
    flask_thread.start()

    loop = asyncio.get_event_loop()
    loop.create_task(async_scheduler())
    loop.run_forever()
