import asyncio
import aiohttp
from typing import List, Dict
from backend.src import FetchConfig
from backend.src.utils.format_date import format_date
from backend.src.constants import NBP_API_URL


class NbpFetcher:
    """Handles fetching data from nbp api"""

    def __init__(self, fetch_config: FetchConfig):
        self.table_type = fetch_config.table_type
        self.days_to_start = fetch_config.days_to_start
        self.days_to_end = fetch_config.days_to_end
        self.currency_to_fetch = fetch_config.currency_to_fetch
        self.url_list = []

    def get_tasks(self, session):
        """Creates tasks list for async execution"""
        tasks = []
        for url in self.url_list:
            tasks.append(asyncio.create_task(session.get(url, ssl=False)))
        return tasks

    def get_urls(self):
        """Creates list of api urls"""
        start_date = format_date(self.days_to_start)
        end_date = format_date(self.days_to_end)

        for currency in self.currency_to_fetch:
            api_parameters = f"{self.table_type}/{currency}/{start_date}/{end_date}/"
            api_url = NBP_API_URL + api_parameters
            self.url_list.append(api_url)

    async def fetch_data(self) -> Dict[str, List[Dict]]:
        """Fetches data asynchronously"""
        fetched_rates = {}

        self.get_urls()
        async with aiohttp.ClientSession() as session:
            tasks = self.get_tasks(session)
            responses = await asyncio.gather(*tasks)
            for currency, response in zip(self.currency_to_fetch, responses):
                result = await response.json()
                fetched_rates[f"{currency.upper()}/PLN"] = result["rates"]

        return fetched_rates
