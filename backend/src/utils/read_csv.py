import os.path
import pandas as pd
import logging
from ..services.cyclic_job import fetch_nbp_api


def read_file(file_path: str) -> pd.DataFrame | None:
    """Reads .csv file with exchange rates and saves it as dataframe"""
    if not os.path.exists(file_path):
        fetch_nbp_api()

    try:
        df = pd.read_csv(file_path)
        df.set_index("Date", inplace=True)
        return df

    except Exception as e:
        logging.error(f"An error occurred while reading exchange rates: {e}")
        return None
