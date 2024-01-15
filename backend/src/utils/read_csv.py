import pandas as pd
import logging


def read_file(file_path: str) -> pd.DataFrame | None:
    """Reads .csv file with exchange rates and saves it as dataframe"""
    try:
        df = pd.read_csv(file_path)
        df.set_index("Date", inplace=True)
        return df

    except Exception as e:
        logging.error(f"An error occurred while reading exchange rates: {e}")
        return None
