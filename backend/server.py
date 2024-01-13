import os.path
import pandas as pd
import logging

from nbp_api import fetch_nbp_api, ALL_CURRENCY_CSV_FILENAME
from typing import List, Dict
from flask import Flask, request
from flask_cors import CORS, cross_origin

SELECTED_CURRENCY_CSV_FILENAME = "selected_currency_data.csv"
app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})


class FileReader:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.exchange_rates_df = None

    def read_file(self) -> None:
        if not os.path.exists(self.file_path):
            fetch_nbp_api()

        try:
            df = pd.read_csv(self.file_path)
            df.set_index("Date", inplace=True)
            self.exchange_rates_df = df

        except Exception as e:
            logging.error(f"An error occurred while reading exchange rates: {e}")
            return None

    def get_plain_df(self) -> pd.DataFrame:
        self.read_file()
        return self.exchange_rates_df

    def get_exchange_rates(self, requested_currencies: List[str]) -> Dict | None:
        self.read_file()
        filtered_df = self.exchange_rates_df.filter(requested_currencies)
        return filtered_df.to_dict()

    def get_currencies_list(self) -> List[str]:
        self.read_file()
        return self.exchange_rates_df.columns.tolist()


file_reader = FileReader(ALL_CURRENCY_CSV_FILENAME)


@app.route("/api/get_currency_types/", methods=["GET"])
def get_currency_types():
    currencies_list = file_reader.get_currencies_list()
    if not currencies_list:
        return {"message": "Error loading exchange rates"}, 500

    return {"message": "CSV file read successfully", "currencies_list": currencies_list}, 200


@app.route("/api/get_exchange_rates/", methods=["GET"])
def get_exchange_rates():
    requested_currencies = request.args.getlist("currencies")

    if not requested_currencies:
        return {"message": "No currencies to query received"}, 404

    exchange_rates = file_reader.get_exchange_rates(requested_currencies)
    if not exchange_rates:
        return {"message": "Error loading exchange rates"}, 500

    return {"message": "CSV file queried successfully", "exchange_rates": exchange_rates}, 200


@app.route("/api/analyze_data/", methods=["GET"])
def analyze_data():
    requested_currencies = request.args.getlist("currencies")

    if not requested_currencies:
        return {"message": "No currencies to query received"}, 404

    df = file_reader.get_plain_df()

    if df is None:
        return {"message": "Error loading exchange rates"}, 500

    filtered_df = df.filter(requested_currencies)
    analyzed_data = {}

    for column_name, column_values in filtered_df.items():
        data_dict = {
            "average_value": round(column_values.mean(), 4),
            "median_value": round(column_values.median(), 4),
            "min_value": round(column_values.min(), 4),
            "max_value": round(column_values.max(), 4)
        }
        analyzed_data[column_name] = data_dict

    return {"message": "Data analyzed successfully", "analyzed_data": analyzed_data}, 200


@app.route("/api/save_exchange_rates/", methods=["POST", "OPTIONS"])
@cross_origin()
def save_exchange_rates():
    if request.is_json:
        try:
            currency_pairs = request.get_json()['currency_pairs']
            df = file_reader.get_plain_df()

            filtered_df = df[currency_pairs]
            filtered_df.to_csv(SELECTED_CURRENCY_CSV_FILENAME)

            return {"message": f"Exchange rates for {currency_pairs} saved "
                               f"successfully to selected_currency_data.csv"}, 200

        except Exception as e:
            return {"message": f"Error while saving exchange rates: {e}"}, 500
    return {"message": "Incorrect request"}, 400
