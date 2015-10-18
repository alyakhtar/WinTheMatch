from flask import Flask, request, render_template
from flaskext.mysql import MySQL


mysql = MySQL()

app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'adityagupta'
app.config['MYSQL_DATABASE_DB'] = 'cricket'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)


@app.route("/login", methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['UserName']
        password = request.form['Password']
        if username == "admin" and password == "admin":
            return render_template('login_success.html')
        else:
            return render_template('login_error.html')


@app.route("/")
def index():
    return render_template('index.html')


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


@app.route("/bowling", methods=['POST', 'GET'])
def bowling():
    if request.method == 'GET':
        cursor = mysql.connect().cursor()
        cursor.execute("SELECT DISTINCT(PLayer) from bowling_statistics")
        player = cursor.fetchall()
        return render_template('bowling.html', player=player)


if __name__ == "__main__":
    app.run(debug=True)
