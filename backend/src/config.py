from typing import List
from pydantic import BaseModel


class FetchConfig(BaseModel):
    """Config for data fetching"""
    table_type: str = "a"
    days_to_start: int = 90
    days_to_end: int = 0
    currency_to_fetch: List[str] = ["eur", "usd", "chf"]


class ProductionConfig(BaseModel):
    """Flask production config"""
    DEBUG: bool = False
    USE_RELOADER: bool = False
    PORT: int = 5000
    HOST: str = "0.0.0.0"


class DevConfig(BaseModel):
    """Flask dev config"""
    DEBUG: bool = True
    USE_RELOADER: bool = False
    PORT: int = 5000
    HOST: str = "0.0.0.0"


class Config(BaseModel):
    """Flask config"""
    dev_config: DevConfig = DevConfig()
    production_config: ProductionConfig = ProductionConfig()
