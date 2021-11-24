import pytest
import app
from controllers import chars

@pytest.fixture
def api(monkeypatch):
    test_chars = [
        {"id": 1, "name": "HULK", "affiliation": ["Umbrella"], "debut": "Test, 2021"},
        {"id": 2, "name": "Zombie", "affiliation": ["Civilian"], "debut": "Test, 2021"}
    ]
    monkeypatch.setattr(chars, "chars", test_chars)
    api = app.app.test_client()
    return api