from bs4 import BeautifulSoup

def test_display_board_bs(client):
    clubs = [
        {
            "name":"Simply Lift",
            "email":"john@simplylift.co",
            "points":"13"
        },
        {
            "name":"Iron Temple",
            "email": "admin@irontemple.com",
            "points":"4"
        },
        {   "name":"She Lifts",
            "email": "kate@shelifts.co.uk",
            "points":"12"
        }
    ]
    response = client.get('/')
    soup = BeautifulSoup(response.text, features="html.parser")
    lis = soup.find_all("li", {"class": "club"})
    clubs_list = []
    for li in lis:
        clubs_list.append(li.text)
    for club in clubs :
        assert f"{club['name']} Points: {club['points']}" in clubs_list

def test_board_status_code_ok(client):
    response = client.get('/')
    assert response.status_code == 200


def test_display_board(client):
    response = client.get('/')
    assert response.status_code == 200
    data = response.data.decode()
    assert ('Simply Lift Points: 13') in data
    assert ('Iron Temple Points: 4') in data
    assert ('She Lifts Points: 12') in data