import pandas as pd

from main import ALL_CURRENCY_CSV_FILENAME
from flask import Flask, request

app = Flask(__name__)


def read_exchange_rates():
    df = pd.read_csv(ALL_CURRENCY_CSV_FILENAME)
    exchange_rates = df.to_dict()
    return exchange_rates


@app.route("/api/get_exchange_rates/", methods=["GET"])
def get_exchange_rates():
    exchange_rates = read_exchange_rates()
    requested_currencies = request.args.getlist("currencies")

    if not requested_currencies:
        return {"message": "No currencies to query received"}, 404

    return {"message": "placeholder"}, 200
