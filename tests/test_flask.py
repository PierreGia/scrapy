import json
from app import app

def test_random_quote():
    client = app.test_client()
    response = client.get('/random_quote')

    assert response.status_code == 200
    data = json.loads(response.get_data(as_text=True))

    assert 'text' in data
    assert 'author' in data
    assert 'tags' in data
