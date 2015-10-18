from flask import Flask, request, render_template
from flask.ext.mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL(app)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/batting", methods=['POST', 'GET'])
def batting():
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        cur.execute('''SELECT user, host FROM mysql.user''')
        rv = cur.fetchall()
        return render_template('batting.html', str(rv))


@app.route("/bowling")
def bowling():
    return render_template('bowling.html')

if __name__ == "__main__":
    app.run(debug=True)
