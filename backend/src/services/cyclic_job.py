from .fetch_nbp import NbpFetcher
from ..utils.save_df import save_df_as_csv
from ..utils.build_df import create_exchange_rates_df, calculate_rates, create_dates_column
from ..constants import ALL_CURRENCY_CSV_FILEPATH
from ..config import FetchConfig

fetch_config = FetchConfig()


def fetch_nbp_api() -> None:
    """Executes fetching and saving data. Used as a cyclic task for scheduler"""

    nbp_fetcher = NbpFetcher(table_type=fetch_config.table_type,
                             days_to_start=fetch_config.days_to_start,
                             days_to_end=fetch_config.days_to_end,
                             currency_to_fetch=fetch_config.currency_to_fetch)

    fetched_rates = nbp_fetcher.get_fetched_rates()

    df = create_dates_column(days_to_start=fetch_config.days_to_start,
                             days_to_end=fetch_config.days_to_end)
    df = create_exchange_rates_df(df=df, exchange_rates=fetched_rates)
    df = calculate_rates(df=df)

    save_df_as_csv(df=df,
                   file_path=ALL_CURRENCY_CSV_FILEPATH)
