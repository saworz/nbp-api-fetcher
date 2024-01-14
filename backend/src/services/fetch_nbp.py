import requests
import logging
from typing import List, Dict
from pydantic import BaseModel
from ..utils.format_date import format_date


class NbpFetcher(BaseModel):
    """Handles fetching data from nbp api"""
    table_type: str
    days_to_start: int
    days_to_end: int

    def fetch(self, currency_name: str) -> List[Dict] | None:
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
