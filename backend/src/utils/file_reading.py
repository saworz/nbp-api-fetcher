import os.path
import pandas as pd
import logging
from .fetch_job import fetch_nbp_api
from typing import List, Dict
from pydantic import BaseModel


class CsvReader(BaseModel):
    """Reads csv file and returns it as pandas dataframe"""
    file_path: str

    def read_file(self) -> pd.DataFrame | None:
        """Reads .csv file with exchange rates and saves it as dataframe"""
        if not os.path.exists(self.file_path):
            fetch_nbp_api()

        try:
            df = pd.read_csv(self.file_path)
            df.set_index("Date", inplace=True)
            return df

        except Exception as e:
            logging.error(f"An error occurred while reading exchange rates: {e}")
            return None


class ExchangeRatesFilter(BaseModel):
    file_path: str

    def get_exchange_rates(self, requested_currencies: List[str]) -> Dict | None:
        """Returns exchange rates as a dictionary"""
        csv_reader = CsvReader(file_path=self.file_path)
        df = csv_reader.read_file()
        filtered_df = df.filter(requested_currencies)
        return filtered_df.to_dict()


class CurrenciesListReader(BaseModel):
    file_path: str

    def get_currencies_list(self) -> List[str]:
        """Returns list of currencies"""
        csv_reader = CsvReader(file_path=self.file_path)
        df = csv_reader.read_file()
        return df.columns.tolist()
