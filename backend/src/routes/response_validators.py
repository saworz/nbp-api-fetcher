from pydantic import BaseModel
from typing import List, Dict


class CurrencyTypesResponse(BaseModel):
    """Response validator class"""
    currencies_list: List[str]
    message: str


class GetExchangeRatesResponse(BaseModel):
    """Response validator class"""
    exchange_rates: Dict[str, Dict[str, float | None]]
    message: str


class AnalyzeDataResponse(BaseModel):
    """Response validator class"""
    analyzed_data: Dict[str, Dict[str, float]]
    message: str
