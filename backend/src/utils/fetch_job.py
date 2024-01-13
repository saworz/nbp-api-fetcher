from .nbp_fetching import NbpFetcher
from .csv_converting import CsvConverter


def fetch_nbp_api() -> None:
    """Executes fetching and saving data. Used as a cyclic task for scheduler"""
    fetch_config = {
        "table_type": "a",
        "days_to_start": 90,
        "days_to_end": 0,
        "currency_to_fetch": ["eur", "usd", "chf"]
    }

    nbp_fetcher = NbpFetcher(fetch_config)
    fetched_rates = {}

    for currency in fetch_config["currency_to_fetch"]:
        rates = nbp_fetcher.fetch(currency)
        if rates:
            fetched_rates[f"{currency.upper()}/PLN"] = rates

    csv_converter = CsvConverter(fetched_rates, fetch_config)
    csv_converter.save_rates()