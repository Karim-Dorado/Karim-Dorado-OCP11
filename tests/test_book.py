

def test_book(client):
    name = "Simply Lift"
    competition = "Fall Classic"
    response = client.get(f"/book/{competition}/{name}")
    assert response.status_code == 200