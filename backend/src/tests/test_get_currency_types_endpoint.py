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


def test_get_currency_types_status_code(response):
    assert response.status_code == 200


def test_get_currency_types_content_type(response):
    assert response.content_type == "application/json"


def test_get_currency_types_response_structure(response):
    data = response.get_json()
    assert isinstance(data, dict)


def test_get_currency_types_currencies_type(response):
    data = response.get_json()
    currencies_list = data.get("currencies_list")
    assert all(isinstance(currency, str) for currency in currencies_list)


def test_get_currency_types_message_type(response):
    data = response.get_json()
    message = data.get("message")
    assert isinstance(message, str)
