import pytest
from .. import app


@pytest.fixture
def client():
    return app.test_client()
#
#
# def test_analyze_data_status_code(client):
#     with client as c:
#         rv = c.get("/api/analyze_data/")
#         assert rv.status_code == 200
#
#
# def test_analyze_data_content_type(client):
#     with client as c:
#         rv = c.get("/api/get_currency_types/")
#         assert rv.content_type == "application/json"
