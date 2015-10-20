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
    print info
    return render_template('news.html', info=info)


@app.route("/about")
def about():
    return render_template('about.html')


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
        # from Extract_data_Batting import win_count
        batsmen = request.form.get('batsmen')
        print batsmen
        # return batsmen
        # r = win_count(batsmen)
        # print batsmen
        return render_template('result_batting.html', batsmen=batsmen)


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
        # from Extract_data_Batting import win_count
        bowler = request.form.get('bowler')
        print bowler
        # return batsmen
        # r = win_count(batsmen)
        # print batsmen
        return render_template('result_bowling.html', bowler=bowler)


if __name__ == "__main__":
    app.run(debug=True)
