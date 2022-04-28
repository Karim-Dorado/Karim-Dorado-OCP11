

def test_book(client):
    email = "john@simplylift.co"
    name = "Simply Lift"
    competition = "Fall Classic"
    login = client.post('/showSummary', data={"email": email,"name": name}, follow_redirects=True)
    assert login.status_code == 200
    response = client.get(f"/book/{competition}/{name}")
    assert response.status_code == 200