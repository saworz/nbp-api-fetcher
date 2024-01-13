from ..constants import ALL_CURRENCY_CSV_FILENAME
from .file_reading import CurrenciesListReader, ExchangeRatesFilter, CsvReader

currencies_reader = CurrenciesListReader(file_path=ALL_CURRENCY_CSV_FILENAME)
exchange_rates_filter = ExchangeRatesFilter(file_path=ALL_CURRENCY_CSV_FILENAME)
csv_reader = CsvReader()
