import pandas as pd
from datetime import datetime, timedelta
from pydantic import BaseModel
from typing import Dict, List


def create_dates_column(days_to_start: int, days_to_end: int) -> pd.DataFrame:
    """Returns the dataframe with dates column"""
    dates_range = [datetime.now() - timedelta(days=i) for i in
                   range(days_to_start - 1, days_to_end - 1, -1)]

    formatted_dates = [date.strftime("%Y-%m-%d") for date in dates_range]
    return pd.DataFrame({"Date": formatted_dates})


def calculate_rates(df: pd.DataFrame) -> pd.DataFrame:
    """Calculates new rates using already existing ones"""
    df["EUR/USD"] = (df["EUR/PLN"] / df["USD/PLN"]).round(4)
    df["CHF/USD"] = (df["CHF/PLN"] / df["USD/PLN"]).round(4)
    return df


def create_exchange_rates_df(df: pd.DataFrame, exchange_rates: Dict[str, List[Dict]]) -> pd.DataFrame:
    """Returns dataframe ready to save as csv"""

    for currency_key, currency_data in exchange_rates.items():
        rates_df = pd.DataFrame(currency_data)
        merged_df = pd.merge(df, rates_df, how="left", left_on="Date", right_on="effectiveDate")
        merged_df.rename(columns={"mid": currency_key}, inplace=True)
        df[currency_key] = merged_df[currency_key]

    return df
