import pandas as pd
import schedule
from typing import List, Dict
from flask import Flask, request

ALL_CURRENCY_CSV_FILENAME = "all_currency_data.csv"
SELECTED_CURRENCY_CSV_FILENAME = "selected_currency_data.csv"
app = Flask(__name__)


def read_exchange_rates(requested_currencies: List[str]) -> Dict:
    df = pd.read_csv(ALL_CURRENCY_CSV_FILENAME)
    df.set_index("Date", inplace=True)
    filtered_df = df.filter(requested_currencies)
    return filtered_df.to_dict()


@app.route("/api/get_exchange_rates/", methods=["GET"])
def get_exchange_rates():
    requested_currencies = request.args.getlist("currencies")

    if not requested_currencies:
        return {"message": "No currencies to query received"}, 404

    exchange_rates = read_exchange_rates(requested_currencies)
    if not exchange_rates:
        return {"message": "Error loading exchange rates"}, 500

    return {"message": "CSV file queried successfully", "exchange_rates": exchange_rates}, 200


@app.route("/api/save_exchange_rates/", methods=["POST"])
def save_exchange_rates():
    if request.is_json:
        exchange_rates = request.get_json()['exchange_rates']
        df = pd.DataFrame.from_dict(exchange_rates)
        df.to_csv(SELECTED_CURRENCY_CSV_FILENAME)
        return {"message": "Exchange rates saved successfully to selected_currency_data.csv"}, 200
    return {"message": "Incorrect request"}, 400


def fetch_nbp():
    print('hello')


