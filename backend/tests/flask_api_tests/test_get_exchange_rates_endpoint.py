import pytest
from . import client
from .test_api_mock_data import generate_fake_data


@pytest.fixture
def response(client, tmpdir):
    temp_dir = tmpdir.mkdir("temp_dir")

    with temp_dir.as_cwd():
        generate_fake_data()
        return client.get("/api/get_exchange_rates/?currencies=USD/PLN&currencies=EUR/PLN")


def test_get_exchange_rates_empty_request(client):
    response = client.get("/api/get_exchange_rates/")
    assert response.status_code == 400


def test_get_exchange_rates_response(response):
    assert response.status_code == 200


def test_exchange_rates_type(response):
    data = response.get_json()
    analyzed_data = data.get("exchange_rates")
    assert isinstance(analyzed_data, dict)

    for currency_name, info in analyzed_data.items():
        assert isinstance(currency_name, str)

        for date, value in info.items():
            assert isinstance(date, str)
            assert isinstance(value, float)
