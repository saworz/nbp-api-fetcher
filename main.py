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


def get_mid_values(rates):
    return [entry['mid'] for entry in rates]


if __name__ == '__main__':
    fetcher = NbpFetcher(table_type="a", days_to_start=90, days_to_end=0)
    eur_rates = fetcher.fetch(currency="eur")
    usd_rates = fetcher.fetch(currency="usd")
    chf_rates = fetcher.fetch(currency="chf")

    print(chf_rates['rates'])
    # df = pd.DataFrame({"EUR/PLN": get_mid_values(eur_rates["rates"]),
    #                    "USD/PLN": get_mid_values(usd_rates["rates"]),
    #                    "CHF/PLN": get_mid_values(chf_rates["rates"])})

    # print(df)
