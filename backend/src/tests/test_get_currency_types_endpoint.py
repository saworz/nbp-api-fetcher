import pytest
from .. import app


@pytest.fixture
def client():
    return app.test_client()


@pytest.fixture
def response(client, tmpdir):
    temp_dir = tmpdir.mkdir("temp_dir")

    with temp_dir.as_cwd():
        return client.get("/api/get_currency_types/")


def test_get_currency_types_response(response):
    assert response.status_code == 200
    assert response.content_type == "application/json"


def test_get_currency_types_response_structure(response):
    data = response.get_json()
    assert isinstance(data, dict)


def test_get_currency_types_currencies_type(response):
    data = response.get_json()
    currencies_list = data.get("currencies_list")
    assert all(isinstance(currency, str) for currency in currencies_list)
