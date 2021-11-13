import pytest
import requests

# Test: main page
# Result: 200
def test1():
    response = requests.get("http://localhost:15100")
    assert response.status_code == 200

