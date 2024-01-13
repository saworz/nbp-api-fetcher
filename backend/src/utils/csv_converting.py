import os.path
import pandas as pd
import logging
from datetime import datetime, timedelta
from ..constants import ALL_CURRENCY_CSV_FILENAME
from pydantic import BaseModel
from typing import Dict, List


class DfDateColumnGenerator(BaseModel):
    days_to_start: int
    days_to_end: int

    def get_dates_column(self) -> pd.DataFrame:
        """Returns the dataframe with dates column"""
        dates_range = [datetime.now() - timedelta(days=i) for i in
                       range(self.days_to_start - 1, self.days_to_end - 1, -1)]

        formatted_dates = [date.strftime("%Y-%m-%d") for date in dates_range]
        return pd.DataFrame({"Date": formatted_dates})


class ExchangeRate(BaseModel):
    no: str
    effectiveDate: str
    mid: float


class ExchangeRatesDfBuilder(BaseModel):
    days_to_start: int
    days_to_end: int
    exchange_rates: Dict[str, List[ExchangeRate]]

    @staticmethod
    def calculate_rates(df: pd.DataFrame) -> pd.DataFrame:
        """Calculates new rates using already existing ones"""
        df["EUR/USD"] = (df["EUR/PLN"] / df["USD/PLN"]).round(4)
        df["CHF/USD"] = (df["CHF/PLN"] / df["USD/PLN"]).round(4)
        return df

    def create_rates_df(self) -> pd.DataFrame:
        """Returns dataframe ready to save as csv"""

        date_generator = DfDateColumnGenerator(days_to_start=self.days_to_start,
                                               days_to_end=self.days_to_end)
        df = date_generator.get_dates_column()

        for currency_key, currency_data in self.exchange_rates.items():
            transformed_data = [rate.model_dump() for rate in currency_data]
            rates_df = pd.DataFrame(transformed_data)
            merged_df = pd.merge(df, rates_df, how="left", left_on="Date", right_on="effectiveDate")
            merged_df.rename(columns={"mid": currency_key}, inplace=True)
            df[currency_key] = merged_df[currency_key]

        df = self.calculate_rates(df)
        return df


class ExchangeRatesSaver(BaseModel):
    """Handles saving data to .csv file"""
    df: pd.DataFrame

    class Config:
        arbitrary_types_allowed = True

    def save_rates_as_csv(self) -> None:
        """Saves dataframe to .csv"""
        if self.df.empty:
            logging.error("No exchange rates to save")
            return

        try:
            if os.path.exists(ALL_CURRENCY_CSV_FILENAME):
                logging.debug(f"{ALL_CURRENCY_CSV_FILENAME} already exists, concatenating dataframes")
                existing_df = pd.read_csv(ALL_CURRENCY_CSV_FILENAME)
                self.df = pd.concat([existing_df, self.df]).drop_duplicates(subset=["Date"], keep="last")

            self.df.to_csv(ALL_CURRENCY_CSV_FILENAME, index=False)
            logging.info("Data saved to all_currency_data.csv successfully.")
        except Exception as e:
            logging.error(f"Error while saving data to all_currency_data.csv: {e}")
