from .nbp_fetching import NbpFetcher
from .csv_converting import ExchangeRatesSaver, ExchangeRatesDfBuilder


def fetch_nbp_api() -> None:
    """Executes fetching and saving data. Used as a cyclic task for scheduler"""
    fetch_config = {
        "table_type": "a",
        "days_to_start": 90,
        "days_to_end": 0,
        "currency_to_fetch": ["eur", "usd", "chf"]
    }

    nbp_fetcher = NbpFetcher(table_type=fetch_config["table_type"],
                             days_to_start=fetch_config["days_to_start"],
                             days_to_end=fetch_config["days_to_end"]
                             )

    fetched_rates = {}

    for currency in fetch_config["currency_to_fetch"]:
        rates = nbp_fetcher.fetch(currency)
        if rates:
            fetched_rates[f"{currency.upper()}/PLN"] = rates

    exchange_rates_converter = ExchangeRatesDfBuilder(exchange_rates=fetched_rates,
                                                      days_to_start=fetch_config["days_to_start"],
                                                      days_to_end=fetch_config["days_to_end"]
                                                      )

    df = exchange_rates_converter.create_rates_df()

    exchange_rates_saver = ExchangeRatesSaver(df=df)
    exchange_rates_saver.save_rates_as_csv()
