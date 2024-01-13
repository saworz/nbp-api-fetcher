import requests
import logging
from typing import List, Dict
from datetime import datetime, timedelta
from pydantic import BaseModel


class NbpFetcher(BaseModel):
    """Handles fetching data from nbp api"""
    table_type: str
    days_to_start: int
    days_to_end: int

    @staticmethod
    def format_date(days_delta: int) -> str:
        """Return date days_delta prior to today in format YYYY-MM-DD"""
        date = datetime.now() - timedelta(days=days_delta)
        return date.strftime("%Y-%m-%d")

    def fetch(self, currency_name: str) -> List[Dict] | None:
        """Fetches data from nbp api and returns it as a list of dicts"""
        start_date = self.format_date(self.days_to_start)
        end_date = self.format_date(self.days_to_end)
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
