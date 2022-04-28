import pytest
import server


@pytest.fixture
def client():
    server.app.config['TESTING'] = True
    clients = server.app.test_client()
    return clients

    
def test_valid_email(client):
    email = "john@simplylift.co"
    response = client.post('/showSummary', data={"email": email})
    assert response.status_code == 200
    assert ("Welcome, " + email) in response.data.decode()


def test_invalid_email(client):
	response = client.post('/showSummary', data={"email": "test@test.com"})
	assert response.status_code == 200
	assert ("Invalid email adress !") in response.data.decode()

def test_empty_email(client):
    response = client.post('/showSummary', data = {"email": ""})
    assert response.status_code == 200
    assert ("Invalid email adress !") in response.data.decode()
