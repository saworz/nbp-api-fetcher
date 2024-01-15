import os
import pytest
from .. import app
import pandas as pd
from ..constants import ALL_CURRENCY_CSV_FILEPATH


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


@pytest.fixture
def response(client, tmpdir):
    temp_dir = tmpdir.mkdir("temp_dir")

    with temp_dir.as_cwd():
        generate_fake_data()
        return client.get("/api/analyze_data/?currencies=USD/PLN&currencies=EUR/PLN")


def test_analyze_data_empty_request(client):
    response = client.get("/api/analyze_data/")
    assert response.status_code == 400


def test_analyze_data_response(response):
    assert response.status_code == 200


def test_analyzed_data_type(response):
    data = response.get_json()
    analyzed_data = data.get("analyzed_data")
    assert isinstance(analyzed_data, dict)

    for currency_name, info in analyzed_data.items():
        assert isinstance(currency_name, str)

        for indicator, value in info.items():
            assert isinstance(indicator, str)
            assert isinstance(value, float)
