import os.path
import pandas as pd
import logging
from datetime import datetime, timedelta
from ..constants import ALL_CURRENCY_CSV_FILENAME
from pydantic import BaseModel
from typing import Dict, List


class CsvConverter(BaseModel):
    """Handles saving data to .csv file"""
    days_to_start: int
    days_to_end: int
    exchange_rates: Dict[str, List[Dict]]

    def get_dates_column(self) -> pd.DataFrame:
        """Returns the dataframe with dates column"""
        dates_range = [datetime.now() - timedelta(days=i) for i in
                       range(self.days_to_start - 1, self.days_to_end - 1, -1)]

        formatted_dates = [date.strftime("%Y-%m-%d") for date in dates_range]
        return pd.DataFrame({"Date": formatted_dates})

    @staticmethod
    def calculate_rates(df: pd.DataFrame) -> pd.DataFrame:
        """Calculates new rates using already existing ones"""
        df["EUR/USD"] = (df["EUR/PLN"] / df["USD/PLN"]).round(4)
        df["CHF/USD"] = (df["CHF/PLN"] / df["USD/PLN"]).round(4)
        return df

    def create_rates_df(self) -> pd.DataFrame:
        """Returns dataframe ready to save as csv"""
        df = self.get_dates_column()

        for currency_key, currency_value in self.exchange_rates.items():
            rates_df = pd.DataFrame(currency_value)
            merged_df = pd.merge(df, rates_df, how="left", left_on="Date", right_on="effectiveDate")
            merged_df.rename(columns={"mid": currency_key}, inplace=True)
            df[currency_key] = merged_df[currency_key]

        df = self.calculate_rates(df)
        return df

    def save_rates(self) -> None:
        """Saves dataframe to .csv"""
        if len(self.exchange_rates) == 0:
            logging.error("No exchange rates to save")
            return

        df = self.create_rates_df()
        try:
            if os.path.exists(ALL_CURRENCY_CSV_FILENAME):
                logging.debug(f"{ALL_CURRENCY_CSV_FILENAME} already exists, concatenating dataframes")
                existing_df = pd.read_csv(ALL_CURRENCY_CSV_FILENAME)
                df = pd.concat([existing_df, df]).drop_duplicates(subset=["Date"], keep="last")

            df.to_csv(ALL_CURRENCY_CSV_FILENAME, index=False)
            logging.info("Data saved to all_currency_data.csv successfully.")
        except Exception as e:
            logging.error(f"Error while saving data to all_currency_data.csv: {e}")
