import asyncio
from backend.src.services.cyclic_job import fetch_nbp_api


def call_fetch_task() -> None:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(fetch_nbp_api())
