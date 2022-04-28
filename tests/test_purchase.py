

def test_success_booking_places(client):
    club = "Simply Lift"
    email = "john@simplylift.co"
    competition = "Fall Classic"
    login = client.post('/showSummary',  data={"email": email, "name": club}, follow_redirects=True)
    assert login.status_code == 200
    response = client.post(
        '/purchasePlaces',
        data={
            'club':club,
            'competition':competition,
            'places':10
            }
    )
    assert response.status_code == 200
    data = response.data.decode()
    assert data.find("Great-booking complete!")


def test_to_much_booking_places(client):
    club = "Iron Temple"
    email = "admin@irontemple.com"
    competition = "Fall Classic"
    login = client.post('/showSummary',  data={"email": email, "name": club}, follow_redirects=True)
    assert login.status_code == 200
    response = client.post(
        '/purchasePlaces',
        data={
            'club':club,
            'competition':competition,
            'places':6
            }
    )
    assert response.status_code == 200
    data = response.data.decode()
    assert data.find("Not enough points to require this number of places!")


def test_fail_negative_booking_places(client):
    club = "Simply Lift"
    email = "john@simplylift.co"
    competition = "Fall Classic"
    login = client.post('/showSummary',  data={"email": email, "name": club}, follow_redirects=True)
    assert login.status_code == 200
    response = client.post(
        '/purchasePlaces',
        data={
            'club':club,
            'competition':competition,
            'places':-1
            }
    )
    assert response.status_code == 200
    data = response.data.decode()
    assert data.find("Please, enter a positive number!")

def test_purchase_more_than_12_places(client):
    club = "Simply Lift"
    email = "john@simplylift.co"
    competition = "Fall Classic"
    login = client.post('/showSummary',  data={"email": email, "name": club}, follow_redirects=True)
    assert login.status_code == 200
    response = client.post(
        '/purchasePlaces',
        data={
            'club':club,
            'competition':competition,
            'places':13
            }
    )
    assert response.status_code == 200
    data = response.data.decode()
    assert data.find("You can't require more than 12 places")