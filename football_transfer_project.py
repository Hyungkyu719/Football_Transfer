from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/')
@app.route('/football_transfer')
def football_transfer():
    return render_template('main.html')

@app.route('/football_transfer/transfer_data')
def transfer_data():
    return render_template('select_data_type.html',data='transfer')

@app.route('/football_transfer//transfer_data/full_transfer_data')
def full_transfer_data():
    db = sqlite3.connect("Football_transfer.db")
    db.row_factory = sqlite3.Row
    items = db.execute(
        'SELECT Player, Window, Position, Country, "From", "To", Description, Price, League FROM transfer_data'
    ).fetchall()
    db.close()
    return render_template('full_transfer_data.html', items=items)

@app.route('/football_transfer/league_data')
def league_data():
    return render_template('select_data_type.html',data='league')


@app.route('/football_transfer/league_data/ligue1',methods=['GET','POST'])
def ligue1():
    ligue1=f"Ligue1"
    if request.method == 'POST' :
        team = request.form['name']
        db = sqlite3.connect("Football_transfer.db")
        db.row_factory = sqlite3.Row
        team=f"%{team}%"
        items = db.execute(
        'SELECT * FROM FullData,League WHERE League.Fname = FullData.Club and Lname = :ligue1 and Club like :team order by club',{"ligue1":ligue1, "team":team}
        ).fetchall()
        db.close()
        return render_template('show_team.html',league='ligue1', mode='show', items=items)
    else :
        db = sqlite3.connect("Football_transfer.db")
        db.row_factory = sqlite3.Row
        items = db.execute(
        'SELECT * FROM League WHERE Lname = :ligue1', {"ligue1":ligue1}
        ).fetchall()
        db.close()
        return render_template('show_team.html', league='ligue1', mode='find', items=items)

@app.route('/football_transfer/league_data/laliga',methods=['GET','POST'])
def laliga():
    laliga=f"LaLiga"
    if request.method == 'POST' :
        team = request.form['name']
        db = sqlite3.connect("Football_transfer.db")
        db.row_factory = sqlite3.Row
        team=f"%{team}%"
        items = db.execute(
        'SELECT * FROM FullData,League WHERE League.Fname = FullData.Club and Lname = :laliga and Club like :team order by club',{"laliga":laliga, "team":team}
        ).fetchall()
        db.close()
        return render_template('show_team.html',league='laliga', mode='show', items=items)
    else :
        db = sqlite3.connect("Football_transfer.db")
        db.row_factory = sqlite3.Row
        items = db.execute(
        'SELECT * FROM League WHERE Lname = :laliga', {"laliga":laliga}
        ).fetchall()
        db.close()
        return render_template('show_team.html', league='laliga', mode='find', items=items)

@app.route('/football_transfer/league_data/epl',methods=['GET','POST'])
def epl():
    epl=f"EPL"
    if request.method == 'POST' :
        team = request.form['name']
        db = sqlite3.connect("Football_transfer.db")
        db.row_factory = sqlite3.Row
        team=f"%{team}%"
        items = db.execute(
        'SELECT * FROM FullData,League WHERE League.Fname = FullData.Club and Lname = :epl and Club like :team order by club',{"epl":epl, "team":team}
        ).fetchall()
        db.close()
        return render_template('show_team.html',league='epl', mode='show', items=items)
    else :
        db = sqlite3.connect("Football_transfer.db")
        db.row_factory = sqlite3.Row
        items = db.execute(
        'SELECT * FROM League WHERE Lname = :epl', {"epl":epl}
        ).fetchall()
        db.close()
        return render_template('show_team.html', league='epl', mode='find', items=items)


@app.route('/football_transfer/league_data/bundesliga',methods=['GET','POST'])
def bundesliga():
    bundesliga=f"Bundesliga"
    if request.method == 'POST' :
        team = request.form['name']
        db = sqlite3.connect("Football_transfer.db")
        db.row_factory = sqlite3.Row
        team=f"%{team}%"
        items = db.execute(
        'SELECT * FROM FullData,League WHERE League.Fname = FullData.Club and Lname = :bundesliga and Club like :team order by club',{"bundesliga":bundesliga, "team":team}
        ).fetchall()
        db.close()
        return render_template('show_team.html',league='bundesliga', mode='show', items=items)
    else :
        db = sqlite3.connect("Football_transfer.db")
        db.row_factory = sqlite3.Row
        items = db.execute(
        'SELECT * FROM League WHERE Lname= :bundesliga', {"bundesliga":bundesliga}
        ).fetchall()
        db.close()
        return render_template('show_team.html', league='bundesliga', mode='find', items=items)

@app.route('/football_transfer/league_data/seriea',methods=['GET','POST'])
def seriea():
    seriea=f"SerieA"
    if request.method == 'POST' :
        team = request.form['name']
        db = sqlite3.connect("Football_transfer.db")
        db.row_factory = sqlite3.Row
        team=f"%{team}%"
        items = db.execute(
        'SELECT * FROM FullData,League WHERE League.Fname = FullData.Club and Lname = :seriea and Club like :team order by club',{"seriea":seriea, "team":team}
        ).fetchall()
        db.close()
        return render_template('show_team.html',league='seriea', mode='show', items=items)
    else :
        db = sqlite3.connect("Football_transfer.db")
        db.row_factory = sqlite3.Row
        items = db.execute(
        'SELECT * FROM League WHERE Lname = :seriea', {"seriea":seriea}
        ).fetchall()
        db.close()
        return render_template('show_team.html', league='seriea', mode='find', items=items)
    

@app.route('/football_transfer/transfer_data/search_player',methods=['GET','POST'])
def search_player():
    if request.method == 'POST' :
        player = request.form['name']
        db = sqlite3.connect("Football_transfer.db")
        db.row_factory = sqlite3.Row
        player=f"%{player}%"
        items = db.execute(
        'SELECT * FROM transfer_data WHERE player like :player', {"player":player}
        ).fetchall()
        db.close()
        return render_template('search_name.html', mode='player', items=items)
    
    else :
        return render_template('search_name.html', mode='player')


@app.route('/football_transfer/transfer_data/search_team',methods=['GET','POST'])
def search_team():
    if request.method == 'POST' :
        team = request.form['name']
        db = sqlite3.connect("Football_transfer.db")
        db.row_factory = sqlite3.Row
        team=f"%{team}%"
        items = db.execute(
        'SELECT * FROM transfer_data WHERE "TO" like :team', {"team":team}
        ).fetchall()
        db.close()
        return render_template('search_name.html',mode='team', items=items)
    
    else :
        return render_template('search_name.html',mode='team')


@app.route('/football_transfer/transfer_data/search_league',methods=['GET','POST'])
def search_league():
    if request.method == 'POST' :
        league = request.form['name']
        db = sqlite3.connect("Football_transfer.db")
        db.row_factory = sqlite3.Row
        league=f"%{league}%"
        items = db.execute(
        'SELECT * FROM transfer_data WHERE league like :league', {"league":league}
        ).fetchall()
        db.close()
        return render_template('search_name.html',mode='league', items=items)
    
    else :
        return render_template('search_name.html',mode='league')


if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)
