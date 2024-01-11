import requests
import pandas as pd
from datetime import datetime, timedelta


class NbpFetcher:
    def __init__(self, table_type, days_to_start, days_to_end):
        self.table_type = table_type
        self.days_to_start = days_to_start
        self.days_to_end = days_to_end

    @staticmethod
    def format_date(days_delta):
        date = datetime.now() - timedelta(days=days_delta)
        return date.strftime("%Y-%m-%d")

    def fetch(self, currency):
        start_date = self.format_date(self.days_to_start)
        end_date = self.format_date(self.days_to_end)
        api_url = f"http://api.nbp.pl/api/exchangerates/rates/{self.table_type}/{currency}/{start_date}/{end_date}/"

        try:
            response = requests.get(api_url)

            if response.status_code == 200:
                data = response.json()
                return data
            else:
                print(f"Error: Unable to fetch data. Status code: {response.status_code}")
                return

        except Exception as e:
            print(f"An error occurred: {e}")
            return


class CsvConverter(NbpFetcher):
    def __init__(self, exchange_rates, fetcher_instance):
        super().__init__(fetcher_instance.table_type, fetcher_instance.days_to_start, fetcher_instance.days_to_end)
        self.exchange_rates = exchange_rates

    def get_dates_column(self):
        dates_range = [datetime.now() - timedelta(days=i) for i in range(self.days_to_start, self.days_to_end, -1)]
        formatted_dates = [date.strftime("%Y-%m-%d") for date in dates_range]
        return pd.DataFrame({"Date": formatted_dates})

    @staticmethod
    def get_mid_values(rates):
        return [entry['mid'] for entry in rates]

    def create_rates_df(self):
        df = self.get_dates_column()

        for key, value in self.exchange_rates.items():
            rates_df = pd.DataFrame(value)
            merged_df = pd.merge(df, rates_df, how='left', left_on='Date', right_on='effectiveDate')
            merged_df.rename(columns={'mid': key}, inplace=True)
            df[key] = merged_df[key]

        return df

    def save_rates(self):
        df = self.create_rates_df()
        print(df)

if __name__ == '__main__':
    fetcher = NbpFetcher(table_type="a", days_to_start=90, days_to_end=0)

    fetched_rates = {
        "EUR/PLN": fetcher.fetch(currency="eur")["rates"],
        "USD/PLN": fetcher.fetch(currency="usd")["rates"],
        "CHF/PLN": fetcher.fetch(currency="chf")["rates"]
    }

    csv_converter = CsvConverter(exchange_rates=fetched_rates, fetcher_instance=fetcher)
    csv_converter.save_rates()
