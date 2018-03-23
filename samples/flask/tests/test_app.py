import json

import pytest

from wsgi import application


@pytest.fixture()
def application_client():
    return application.test_client()


def test_welcome(application_client):
    response = app_client.get('/api/1.0/welcome')
    payload = json.loads(response.data.decode('utf-8'))

    assert response.status_code == 200
    assert 'message' in payload
