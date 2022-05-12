

def test_success_booking_places(client):
    club = "Simply Lift"
    competition = "Fall Classic"
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
    assert data.find("Great-booking complete!")


def test_not_enough_points(client):
    club = "Iron Temple"
    competition = "Fall Classic"
    response = client.post(
        '/purchasePlaces',
        data={
            'club':club,
            'competition':competition,
            'places':8
            }
    )
    assert response.status_code == 200
    data = response.data.decode()
    assert data.find("Not enough points to require this number of places!")


def test_purchase_negative_places(client):
    club = "Simply Lift"
    competition = "Fall Classic"
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
    competition = "Fall Classic"
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