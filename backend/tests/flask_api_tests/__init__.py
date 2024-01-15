import pytest
from backend.src import app


@pytest.fixture
def client():
    return app.test_client()
