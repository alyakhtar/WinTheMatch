from flask import Flask, request, render_template
from flaskext.mysql import MySQL


mysql = MySQL()

app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'adityagupta'
app.config['MYSQL_DATABASE_DB'] = 'cricket'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)

conn = mysql.connect()

cursor = conn.cursor()


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


@app.route("/batting")
def batting():
    return render_template('batting.html')


@app.route("/bowling")
def bowling():
    return render_template('bowling.html')

if __name__ == "__main__":
    app.run(debug=True)
