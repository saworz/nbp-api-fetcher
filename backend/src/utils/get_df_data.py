import pandas as pd
from typing import List, Dict


def get_filtered_df_as_dict(df: pd.DataFrame, requested_currencies: List[str]) -> Dict | None:
    """Returns exchange rates as a dictionary"""
    filtered_df = df.filter(requested_currencies)
    return filtered_df.to_dict()


def get_df_columns_names(df: pd.DataFrame) -> List[str]:
    """Returns list of currencies"""
    return df.columns.tolist()
