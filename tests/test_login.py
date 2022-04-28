
def test_valid_email(client):
    email = "john@simplylift.co"
    name = "Simply Lift"
    response = client.post('/showSummary', data={"email": email, "name": name})
    assert response.status_code == 200
    assert ("Welcome, " + name) in response.data.decode()


def test_invalid_email(client):
	response = client.post('/showSummary', data={"email": "test@test.com"})
	assert response.status_code == 200
	assert ("Invalid email adress !") in response.data.decode()

def test_empty_email(client):
    response = client.post('/showSummary', data = {"email": ""})
    assert response.status_code == 200
    assert ("Invalid email adress !") in response.data.decode()
