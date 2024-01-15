import pytest
import pandas as pd
import os
from ..constants import ALL_CURRENCY_CSV_FILEPATH
from .. import app


@pytest.fixture
def client():
    return app.test_client()


def generate_fake_data():
    data = {
        "Date": ["2022-01-01", "2022-01-02", "2022-01-03"],
        "EUR/PLN": [4.25, 4.30, 4.28],
        "USD/PLN": [3.60, 3.65, 3.62],
        "CHF/PLN": [3.90, 3.95, 3]
    }

    df = pd.DataFrame(data)
    data_dir, filename = os.path.split(ALL_CURRENCY_CSV_FILEPATH)
    os.makedirs(data_dir, exist_ok=True)
    df.to_csv(ALL_CURRENCY_CSV_FILEPATH, index=False)
