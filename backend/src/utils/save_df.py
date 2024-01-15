import os.path
import pandas as pd
import logging


def save_df_as_csv(df: pd.DataFrame, file_path: str) -> None:
    """Handles saving dataframe to .csv file"""
    if df.empty:
        raise Exception("No exchange rates to save")

    try:
        data_dir, filename = os.path.split(file_path)

        if os.path.exists(file_path):
            logging.debug(f"{file_path} already exists, concatenating dataframes")
            existing_df = pd.read_csv(file_path)
            df = pd.concat([existing_df, df]).drop_duplicates(subset=["Date"], keep="last")

        if not os.path.exists(data_dir):
            os.makedirs(data_dir)

        df.to_csv(file_path, index=False)
        logging.info(f"Data saved to {file_path} successfully.")
    except Exception as e:
        logging.error(f"Error while saving data to {file_path}: {e}")
