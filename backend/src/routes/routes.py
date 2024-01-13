from flask import Blueprint
from flask import request
from flask_cors import cross_origin
from ..utils import file_reader
from ..constants import SELECTED_CURRENCY_CSV_FILENAME
routes = Blueprint('routes', __name__)


@routes.route("/api/get_currency_types/", methods=["GET"])
def get_currency_types():
    """Endpoint for getting list of currency types available"""
    currencies_list = file_reader.get_currencies_list()
    if not currencies_list:
        return {"message": "Error loading exchange rates"}, 500

    return {"message": "CSV file read successfully", "currencies_list": currencies_list}, 200


@routes.route("/api/get_exchange_rates/", methods=["GET"])
def get_exchange_rates():
    """Endpoint for getting exchange rates for currencies provided as url parameters"""
    requested_currencies = request.args.getlist("currencies")

    if not requested_currencies:
        return {"message": "No currencies to query received"}, 404

    exchange_rates = file_reader.get_exchange_rates(requested_currencies)
    if not exchange_rates:
        return {"message": "Error loading exchange rates"}, 500

    return {"message": "CSV file queried successfully", "exchange_rates": exchange_rates}, 200


@routes.route("/api/analyze_data/", methods=["GET"])
def analyze_data():
    """Endpoint for getting analyzed data for currencies provided as url parameters"""
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


@routes.route("/api/save_exchange_rates/", methods=["POST", "OPTIONS"])
@cross_origin()
def save_exchange_rates():
    """Endpoint for saving exchange rates for specified currency pairs"""
    if request.is_json:
        try:
            currency_pairs = request.get_json()["currency_pairs"]
            df = file_reader.get_plain_df()

            filtered_df = df[currency_pairs]
            filtered_df.to_csv(SELECTED_CURRENCY_CSV_FILENAME)

            return {"message": f"Exchange rates for {currency_pairs} saved "
                               f"successfully to selected_currency_data.csv"}, 200

        except Exception as e:
            return {"message": f"Error while saving exchange rates: {e}"}, 500
    return {"message": "Incorrect request"}, 400
