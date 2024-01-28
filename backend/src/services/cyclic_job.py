import logging
from .fetch_nbp import NbpFetcher
from backend.src.utils.save_df import save_df_as_csv
from backend.src.utils.build_df import create_exchange_rates_df, calculate_rates, create_dates_column
from backend.src.constants import ALL_CURRENCY_CSV_FILEPATH
from backend.src.config import FetchConfig


async def fetch_nbp_api() -> None:
    """Executes fetching and saving data. Used as a cyclic task for scheduler"""
    fetch_config = FetchConfig()
    nbp_fetcher = NbpFetcher(fetch_config=fetch_config)
    fetched_rates = await nbp_fetcher.fetch_data()
    df = create_dates_column(days_to_start=fetch_config.days_to_start,
                             days_to_end=fetch_config.days_to_end)
    df = create_exchange_rates_df(df=df, exchange_rates=fetched_rates)
    df = calculate_rates(df=df)

    try:
        save_df_as_csv(df=df,
                       file_path=ALL_CURRENCY_CSV_FILEPATH)
    except Exception as e:
        logging.error(f"No exchange rates to save: {e}")
