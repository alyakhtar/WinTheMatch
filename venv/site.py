from flask import Flask, request, render_template, session, flash
from flaskext.mysql import MySQL


mysql = MySQL()

app = Flask(__name__)
app.config.from_object(__name__)


app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'adityagupta'
app.config['MYSQL_DATABASE_DB'] = 'cricket'
app.config['SECRET_KEY'] = 'development key'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)

app.config.from_envvar('VENV_SETTINGS', silent=True)


@app.route("/login", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['UserName'] != app.config['MYSQL_DATABASE_USER']:
            error = 'Invalid username'
        elif request.form['Password'] != app.config['MYSQL_DATABASE_PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return render_template('admin.html')
    return render_template('login_error.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return render_template('index.html')


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/news")
def news():
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from news LIMIT 5")
    info = cursor.fetchall()
    return render_template('news.html', info=info)


@app.route("/about")
def about():
    return render_template('about.html')

# 6 cases


@app.route("/batting", methods=['POST', 'GET'])
def batting():
    if request.method == 'GET':
        cursor = mysql.connect().cursor()
        cursor.execute("SELECT DISTINCT(Player) from batting_statistics")
        player = cursor.fetchall()
        cursor.execute("SELECT DISTINCT(Ground) from batting_statistics")
        ground = cursor.fetchall()
        cursor.execute("SELECT DISTINCT(Opposition) from batting_statistics")
        opponent = cursor.fetchall()
        return render_template('batting.html', player=player, ground=ground, opponent=opponent)

    else:
        import Extract_data_Batting
        Extract_data_Batting.database()
        # FORM 1
        if request.form.get('btn') == 'form1':
            batsmen = request.form.get('batsmen')
            venue = request.form.get('place')
            opponent = request.form.get('opponent')
            run = request.form.get('runs')
            if batsmen != "Select" and run and venue and opponent != "Select":
                r = Extract_data_Batting.win_combined(batsmen, opponent, run, venue)
            elif batsmen != "Select" and run and venue:
                r = Extract_data_Batting.win_location(batsmen, run, venue)
            elif batsmen != "Select" and run and opponent != "Select":
                r = Extract_data_Batting.win_against(batsmen, run, opponent)
            elif batsmen != "Select" and run:
                r = Extract_data_Batting.win_count(batsmen, run)
            return render_template('result_batting.html', batsmen=batsmen, r=r)
        # FORM 2
        else:
            player = request.form.get('players')
            if player == "option1":
                r = Extract_data_Batting.double_half_century()
            elif player == "option2":
                r = Extract_data_Batting.century()
            else:
                r = Extract_data_Batting.combined_score()
            return render_template('result_batting.html', r=r)


@app.route("/bowling", methods=['POST', 'GET'])
def bowling():
    if request.method == 'GET':
        var = '-'
        cursor = mysql.connect().cursor()
        cursor.execute("SELECT DISTINCT(Player) from bowling_statistics")
        player = cursor.fetchall()
        cursor.execute(
            "SELECT DISTINCT(Type) from bowling_statistics where Type!=%s", (var))
        style = cursor.fetchall()
        return render_template('bowling.html', player=player, style=style)

    else:
        import Extract_Data_Bowling
        Extract_Data_Bowling.database()
        bowler = request.form.get('bowler')
        style = request.form.get('style')
        eco = request.form.get('economy')
        if bowler != "Select" and eco:
            r = Extract_Data_Bowling.win_economy(bowler)
        return render_template('result_bowling.html', bowler=bowler, r=r)


if __name__ == "__main__":
    app.run(debug=True)
