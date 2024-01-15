import pytest
from ...services.cyclic_job import fetch_config
from ...services.fetch_nbp import NbpFetcher


@pytest.fixture
def fetcher_instance():
    return NbpFetcher(table_type=fetch_config.table_type,
                      days_to_start=fetch_config.days_to_start,
                      days_to_end=fetch_config.days_to_end,
                      currency_to_fetch=fetch_config.currency_to_fetch)


def test_nbp_fetched_data(fetcher_instance):
    fetched_rates = fetcher_instance.get_fetched_rates()
    assert isinstance(fetched_rates, dict)
    for currency_pair, data in fetched_rates.items():
        assert isinstance(currency_pair, str)
        assert isinstance(data, list)

        assert all(isinstance(item, dict) for item in data)
