from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
@app.route('/football_transfer')
def football_transfer():
    return render_template('main.html')

@app.route('/football_transfer/transfer_data')
def transfer_data():
    db = sqlite3.connect("Football_transfer.db")
    db.row_factory = sqlite3.Row
    items = db.execute(
        'SELECT Player, Window, Position, Country, "From", "To", Description, Price, League FROM transfer_data'
    ).fetchall()
    db.close()
    return render_template('transfer_data.html', items=items)

@app.route('/football_transfer/select_league')
def select_league():
    return render_template('select_league.html')

@app.route('/football_transfer/select_league/bundesliga')
def bundesliga():
    db = sqlite3.connect("Football_transfer.db")
    db.row_factory = sqlite3.Row
    items = db.execute(
        'SELECT Rate, Fname, Sname, Capacity, GF, GA, GD, Pts FROM Bundesliga'
    ).fetchall()
    db.close()
    return render_template('league_data.html', items=items)

@app.route('/football_transfer/select_league/bundesliga/<int:rate>')
def bundesliga_team(rate):
    db = sqlite3.connect("Football_transfer.db")
    db.row_factory = sqlite3.Row
    items = db.execute(
        'SELECT Name, Nationality, Club, Position, Clubjoin, Height, Weight, PrefferedFoot, Birth FROM FullData, Bundesliga WHERE Club=Fname and Rate=?',(rate,)
    ).fetchall()
    db.close()
    return render_template('full_data.html', items=items)

@app.route('/football_transfer/select_league/epl')
def epl():
    db = sqlite3.connect("Football_transfer.db")
    db.row_factory = sqlite3.Row
    items = db.execute(
        'SELECT Rate, Fname, Sname, Capacity, GF, GA, GD, Pts FROM EPL'
    ).fetchall()
    db.close()
    return render_template('league_data.html', items=items)

@app.route('/football_transfer/select_league/epl/<int:rate>')
def epl_team(rate):
    db = sqlite3.connect("Football_transfer.db")
    db.row_factory = sqlite3.Row
    items = db.execute(
        'SELECT Name, Nationality, Club, Position, Clubjoin, Height, Weight, PrefferedFoot, Birth FROM FullData, EPL WHERE Club=Fname and Rate=?',(rate,)
    ).fetchall()
    db.close()
    return render_template('full_data.html', items=items)

@app.route('/football_transfer/select_league/laliga')
def laliga():
    db = sqlite3.connect("Football_transfer.db")
    db.row_factory = sqlite3.Row
    items = db.execute(
        'SELECT Rate, Fname, Sname, Capacity, GF, GA, GD, Pts FROM LaLiga'
    ).fetchall()
    db.close()
    return render_template('league_data.html', items=items)

@app.route('/football_transfer/select_league/laliga/<int:rate>')
def laliga_team(rate):
    db = sqlite3.connect("Football_transfer.db")
    db.row_factory = sqlite3.Row
    items = db.execute(
        'SELECT Name, Nationality, Club, Position, Clubjoin, Height, Weight, PrefferedFoot, Birth FROM FullData, LaLiga WHERE Club=Fname and Rate=?',(rate,)
    ).fetchall()
    db.close()
    return render_template('full_data.html', items=items)

@app.route('/football_transfer/select_league/ligue1')
def ligue1():
    db = sqlite3.connect("Football_transfer.db")
    db.row_factory = sqlite3.Row
    items = db.execute(
        'SELECT Rate, Fname, Sname, Capacity, GF, GA, GD, Pts FROM Ligue1'
    ).fetchall()
    db.close()
    return render_template('league_data.html', items=items)

@app.route('/football_transfer/select_league/ligue1/<int:rate>')
def ligue1_team(rate):
    db = sqlite3.connect("Football_transfer.db")
    db.row_factory = sqlite3.Row
    items = db.execute(
        'SELECT Name, Nationality, Club, Position, Clubjoin, Height, Weight, PrefferedFoot, Birth FROM FullData, Ligue1 WHERE Club=Fname and Rate=?',(rate,)
    ).fetchall()
    db.close()
    return render_template('full_data.html', items=items)

@app.route('/football_transfer/select_league/seriea')
def seriea():
    db = sqlite3.connect("Football_transfer.db")
    db.row_factory = sqlite3.Row
    items = db.execute(
        'SELECT Rate, Fname, Sname, Capacity, GF, GA, GD, Pts FROM SerieA'
    ).fetchall()
    db.close()
    return render_template('league_data.html', items=items)

@app.route('/football_transfer/select_league/seriea/<int:rate>')
def seriea_team(rate):
    db = sqlite3.connect("Football_transfer.db")
    db.row_factory = sqlite3.Row
    items = db.execute(
        'SELECT Name, Nationality, Club, Position, Clubjoin, Height, Weight, PrefferedFoot, Birth FROM FullData, SerieA WHERE Club=Fname and Rate=?',(rate,)
    ).fetchall()
    db.close()
    return render_template('full_data.html', items=items)

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)
