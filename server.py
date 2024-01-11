import pandas as pd

from typing import List, Dict
from main import ALL_CURRENCY_CSV_FILENAME
from flask import Flask, request

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
    return {"message": "CSV file queried successfully", "exchange_rates": exchange_rates}, 200
