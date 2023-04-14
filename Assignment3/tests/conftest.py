import pytest
from app import app

# defines a client fixture for testing purposes
@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client
