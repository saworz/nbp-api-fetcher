from pydantic import BaseModel
from typing import List


class GetExchangeRatesRequest(BaseModel):
    """Request validator class"""
    currencies: List[str]


class AnalyzeDataRequest(BaseModel):
    """Request validator class"""
    currencies: List[str]


class SaveExchangeRatesRequest(BaseModel):
    """Request validator class"""
    currency_pairs: List[str]
