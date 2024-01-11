import requests
import pandas as pd
import logging
import schedule
import time
from typing import List, Dict
from server import ALL_CURRENCY_CSV_FILENAME
from datetime import datetime, timedelta

logging.basicConfig(level=logging.DEBUG)


class NbpFetcher:
    def __init__(self, table_type, days_to_start, days_to_end):
        self.table_type = table_type
        self.days_to_start = days_to_start
        self.days_to_end = days_to_end

    @staticmethod
    def format_date(days_delta: int) -> str:
        date = datetime.now() - timedelta(days=days_delta)
        return date.strftime("%Y-%m-%d")

    def fetch(self, currency_name: str) -> List[Dict] | None:
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

        except Exception as e:
            logging.error(f"An error occurred: {e}")
            return


class CsvConverter(NbpFetcher):
    def __init__(self, exchange_rates, fetcher_instance):
        super().__init__(fetcher_instance.table_type, fetcher_instance.days_to_start, fetcher_instance.days_to_end)
        self.exchange_rates = exchange_rates

    def get_dates_column(self) -> pd.DataFrame:
        dates_range = [datetime.now() - timedelta(days=i) for i in
                       range(self.days_to_start - 1, self.days_to_end - 1, -1)]

        formatted_dates = [date.strftime("%Y-%m-%d") for date in dates_range]
        return pd.DataFrame({"Date": formatted_dates})

    @staticmethod
    def calculate_rates(df: pd.DataFrame) -> pd.DataFrame:
        df["EUR/USD"] = (df["EUR/PLN"] / df["USD/PLN"]).round(4)
        df["CHF/USD"] = (df["CHF/PLN"] / df["USD/PLN"]).round(4)
        return df

    def create_rates_df(self) -> pd.DataFrame:
        df = self.get_dates_column()

        for key, value in self.exchange_rates.items():
            rates_df = pd.DataFrame(value)
            merged_df = pd.merge(df, rates_df, how="left", left_on="Date", right_on="effectiveDate")
            merged_df.rename(columns={"mid": key}, inplace=True)
            df[key] = merged_df[key]

        df = self.calculate_rates(df)
        return df

    def save_rates(self) -> None:
        if len(self.exchange_rates) == 0:
            logging.error("No exchange rates to save")
            return

        df = self.create_rates_df()
        try:
            df.to_csv(ALL_CURRENCY_CSV_FILENAME, index=False)
            logging.info("Data saved to all_currency_data.csv successfully.")
        except Exception as e:
            logging.error(f"Error while saving data to all_currency_data.csv: {e}")


def fetch_nbp_api():
    logging.info("Starting currency data fetching job")
    fetcher = NbpFetcher(table_type="a", days_to_start=90, days_to_end=0)
    currency_to_fetch = ["eur", "usd", "chf"]
    fetched_rates = {}

    for currency in currency_to_fetch:
        rates = fetcher.fetch(currency)
        if rates:
            fetched_rates[f"{currency.upper()}/PLN"] = rates

    csv_converter = CsvConverter(exchange_rates=fetched_rates, fetcher_instance=fetcher)
    csv_converter.save_rates()
