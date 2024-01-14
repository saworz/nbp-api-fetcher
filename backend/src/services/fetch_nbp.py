import requests
import logging
from typing import List, Dict
from ..utils.format_date import format_date
from ..config import FetchConfig


class NbpFetcher:
    """Handles fetching data from nbp api"""
    def __init__(self, fetch_config: FetchConfig):
        self.table_type = fetch_config.table_type
        self.days_to_start = fetch_config.days_to_start
        self.days_to_end = fetch_config.days_to_end
        self.currency_to_fetch = fetch_config.currency_to_fetch

    def fetch_data(self, currency_name: str) -> List[Dict] | None:
        """Fetches data from nbp api and returns it as a list of dicts"""
        start_date = format_date(self.days_to_start)
        end_date = format_date(self.days_to_end)
        api_url = f"https://api.nbp.pl/api/exchangerates/rates/{self.table_type}/{currency_name}/{start_date}/{end_date}/"

        try:
            response = requests.get(api_url)
            response.raise_for_status()

            if response.status_code == 200:
                data = response.json()
                return data["rates"]
            else:
                logging.error(f"Error: Unable to fetch data. Response: {response.text}")
                return
        except requests.RequestException as e:
            logging.error(f"An error occurred on the API request: {e}")
        except ValueError as e:
            logging.error(f"Error parsing JSON response: {e}")

    def get_fetched_rates(self) -> Dict[str, List[Dict]]:
        fetched_rates = {}

        for currency in self.currency_to_fetch:
            rates = self.fetch_data(currency)
            if rates:
                fetched_rates[f"{currency.upper()}/PLN"] = rates
        return fetched_rates