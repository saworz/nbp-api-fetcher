import os
from flask import Blueprint
from flask_cors import cross_origin
from backend.src.utils.read_csv_timeseries import read_csv_as_df
from backend.src.utils.df_convert import get_rates_dict, get_currencies_list
from backend.src.constants import SELECTED_CURRENCY_CSV_FILEPATH, ALL_CURRENCY_CSV_FILEPATH
from flask_pydantic import validate
from .request_validators import GetExchangeRatesRequest, SaveExchangeRatesRequest, AnalyzeDataRequest
from .response_validators import AnalyzeDataResponse, CurrencyTypesResponse, GetExchangeRatesResponse
from backend.src.services.cyclic_job import fetch_nbp_api

routes = Blueprint('routes', __name__)


@routes.route("/api/get_currency_types/", methods=["GET"])
@validate()
def get_currency_types():
    """Endpoint for getting list of currency types available"""

    if not os.path.exists(ALL_CURRENCY_CSV_FILEPATH):
        fetch_nbp_api()

    df = read_csv_as_df(file_path=ALL_CURRENCY_CSV_FILEPATH)

    if df is None:
        return {"message": "Error loading exchange rates"}, 500

    currencies_list = get_currencies_list(df=df)

    return CurrencyTypesResponse(
        currencies_list=currencies_list,
        message="CSV file read successfully"
    ), 200


@routes.route("/api/get_exchange_rates/", methods=["GET"])
@validate()
def get_exchange_rates(query: GetExchangeRatesRequest):
    """Endpoint for getting exchange rates for currencies provided as url parameters"""
    requested_currencies = query.currencies

    if not requested_currencies:
        return {"message": "No currencies to query received"}, 404

    if not os.path.exists(ALL_CURRENCY_CSV_FILEPATH):
        fetch_nbp_api()

    df = read_csv_as_df(file_path=ALL_CURRENCY_CSV_FILEPATH)

    if df is None:
        return {"message": "Error loading exchange rates"}, 500

    exchange_rates = get_rates_dict(df=df,
                                    requested_currencies=requested_currencies)

    return GetExchangeRatesResponse(
        exchange_rates=exchange_rates,
        message="CSV file queried successfully"), 200


@routes.route("/api/analyze_data/", methods=["GET"])
@validate()
def analyze_data(query: AnalyzeDataRequest):
    """Endpoint for getting analyzed data for currencies provided as url parameters"""
    requested_currencies = query.currencies

    if not requested_currencies:
        return {"message": "No currencies to query received"}, 404

    if not os.path.exists(ALL_CURRENCY_CSV_FILEPATH):
        fetch_nbp_api()

    df = read_csv_as_df(file_path=ALL_CURRENCY_CSV_FILEPATH)

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

    return AnalyzeDataResponse(
        analyzed_data=analyzed_data,
        message="Data analyzed successfully"), 200


@routes.route("/api/save_exchange_rates/", methods=["POST", "OPTIONS"])
@cross_origin()
@validate()
def save_exchange_rates(body: SaveExchangeRatesRequest):
    """Endpoint for saving exchange rates for specified currency pairs"""
    requested_currencies = body.currency_pairs

    if not requested_currencies:
        return {"message": "No currencies to query received"}, 404

    if not os.path.exists(ALL_CURRENCY_CSV_FILEPATH):
        fetch_nbp_api()

    df = read_csv_as_df(file_path=ALL_CURRENCY_CSV_FILEPATH)

    if df is None:
        return {"message": "Error loading exchange rates"}, 500

    filtered_df = df[requested_currencies]

    try:
        filtered_df.to_csv(SELECTED_CURRENCY_CSV_FILEPATH)

        return {"message": f"Exchange rates for {requested_currencies} saved "
                           f"successfully to selected_currency_data.csv"}, 200

    except Exception as e:
        return {"message": f"Error while saving exchange rates: {e}"}, 500
