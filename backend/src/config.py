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
    debug: bool = False
    use_reloader: bool = False
    port: int = 5000
    host: str = "0.0.0.0"
    threaded: bool = True


class DevConfig(BaseModel):
    """Flask dev config"""
    debug: bool = True
    use_reloader: bool = False
    port: int = 5000
    host: str = "0.0.0.0"
    threaded: bool = True


class Config(BaseModel):
    """Flask config"""
    dev_config: DevConfig = DevConfig()
    production_config: ProductionConfig = ProductionConfig()
