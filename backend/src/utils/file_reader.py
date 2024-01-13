import os.path
import pandas as pd
import logging
from nbp_api import fetch_nbp_api
from typing import List, Dict


class FileReader:
    """Handles reading .csv file with exchange rates"""
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.exchange_rates_df = None

    def read_file(self) -> None:
        """Reads .csv file with exchange rates and saves it as dataframe"""
        if not os.path.exists(self.file_path):
            fetch_nbp_api()

        try:
            df = pd.read_csv(self.file_path)
            df.set_index("Date", inplace=True)
            self.exchange_rates_df = df

        except Exception as e:
            logging.error(f"An error occurred while reading exchange rates: {e}")
            return None

    def get_plain_df(self) -> pd.DataFrame:
        """Returns plain dataframe with exchange rates"""
        self.read_file()
        return self.exchange_rates_df

    def get_exchange_rates(self, requested_currencies: List[str]) -> Dict | None:
        """Returns exchange rates as a dictionary"""
        self.read_file()
        filtered_df = self.exchange_rates_df.filter(requested_currencies)
        return filtered_df.to_dict()

    def get_currencies_list(self) -> List[str]:
        """Returns list of currencies"""
        self.read_file()
        return self.exchange_rates_df.columns.tolist()
