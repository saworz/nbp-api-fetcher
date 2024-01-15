from . import client, generate_fake_data


def test_save_exchange_rates_correct_request(client, tmpdir):
    temp_dir = tmpdir.mkdir("temp_dir")

    with temp_dir.as_cwd():
        generate_fake_data()
        request_body = {
            "currency_pairs": [
                "USD/PLN",
                "EUR/PLN"
            ]
        }
        response = client.post("/api/save_exchange_rates/", json=request_body)
        assert response.status_code == 200


def test_save_exchange_rates_empty_request(client):
    response = client.post("/api/save_exchange_rates/")
    assert response.status_code == 415


def test_save_exchange_rates_empty_body(client, tmpdir):
    temp_dir = tmpdir.mkdir("temp_dir")

    with temp_dir.as_cwd():
        generate_fake_data()
        request_body = {}
        response = client.post("/api/save_exchange_rates/", json=request_body)
        assert response.status_code == 400
