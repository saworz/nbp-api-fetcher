from typing import List


class FetchConfig:
    def __init__(self):
        self.table_type: str = "a"
        self.days_to_start: int = 90
        self.days_to_end: int = 0
        self.currency_to_fetch: List[str] = ["eur", "usd", "chf"]


class ProductionConfig:
    def __init__(self):
        self.DEBUG: bool = False
        self.USE_RELOADER: bool = False
        self.PORT: int = 5000
        self.HOST: str = "0.0.0.0"


class DevConfig:
    def __init__(self):
        self.DEBUG: bool = True
        self.USE_RELOADER: bool = False
        self.PORT: int = 5000
        self.HOST: str = "0.0.0.0"


class Config:
    def __init__(self):
        self.dev_config: DevConfig = DevConfig()
        self.production_config: ProductionConfig = ProductionConfig()
