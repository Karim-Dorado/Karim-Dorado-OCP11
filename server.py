import json
from datetime import date, datetime
from flask import Flask, render_template, request, redirect, flash, url_for


def load_clubs():
    with open('clubs.json') as c:
        list_of_clubs = json.load(c)['clubs']
        return list_of_clubs


def load_competitions():
    with open('competitions.json') as comps:
        list_of_competitions = json.load(comps)['competitions']
        return list_of_competitions


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = load_competitions()
clubs = load_clubs()
today = str(datetime.today())


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/showSummary', methods=['POST'])
def show_summary():
    try:
        club = [club for club in clubs if club['email'] == request.form['email']][0]
    except IndexError:
        return render_template('index.html',
                               message="Invalid email adress !",
                               )
    return render_template('welcome.html',
                           club=club,
                           competitions=competitions,
                           today=today
                           )


@app.route('/book/<competition>/<club>')
def book(competition, club):
    found_club = [clb for clb in clubs if clb['name'] == club][0]
    found_competition = [comp for comp in competitions if comp['name'] == competition][0]
    if found_club and found_competition:
        return render_template('booking.html',
                               club=found_club,
                               competition=found_competition
                               )
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html',
                               club=club,
                               competitions=competitions,
                               today=today
                               )


@app.route('/purchasePlaces', methods=['POST'])
def purchase_places():
    competition = [comp for comp in competitions if comp['name'] == request.form['competition']][0]
    club = [clb for clb in clubs if clb['name'] == request.form['club']][0]
    places_required = int(request.form['places'])
    if int(club['points']) < places_required:
        flash("Not enough points to require this number of places!")
    elif places_required <= 0 :
        flash("Please, enter a positive number!")
    elif places_required > 12:
        flash("You can't require more than 12 places")
    else:
        competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - places_required
        club['points'] = int(club['points']) - places_required
        flash('Great-booking complete!')
    return render_template('welcome.html',
                           club=club,
                           competitions=competitions,
                           today=today
                           )


# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))
