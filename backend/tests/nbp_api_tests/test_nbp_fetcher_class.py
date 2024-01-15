import pytest
from backend.src import fetch_config
from backend.src.services.fetch_nbp import NbpFetcher


@pytest.fixture
def fetcher_instance():
    return NbpFetcher(fetch_config=fetch_config)


def test_nbp_fetched_data(fetcher_instance):
    fetched_rates = fetcher_instance.get_fetched_rates()
    assert isinstance(fetched_rates, dict)
    for currency_pair, data in fetched_rates.items():
        assert isinstance(currency_pair, str)
        assert isinstance(data, list)

        assert all(isinstance(item, dict) for item in data)
