import pytest
from . import client, generate_fake_data


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
