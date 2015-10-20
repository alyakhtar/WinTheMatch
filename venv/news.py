import requests
import sys
from bs4 import BeautifulSoup
import MySQLdb as mdb


def news():
    url = 'http://www.espncricinfo.com/ci/content/story/news.html'

    source_code = requests.get(url)

    plain_text = source_code.text

    soup = BeautifulSoup(plain_text, "lxml")

    x = []
    y = []
    z = []
    mt = []

    for div in soup.findAll('div', {'class': 'story-briefwrap'}):
        for h2 in div('h2', {'class': 'story-title'}):
            for a in h2('a'):
                xyz = a.get_text()
                xyz = str(xyz)
                x.append(xyz)

        for p in div('p', {'class': 'story-brief'}):
            pqr = p.text
            pqr = " ".join(pqr.split())
            pqr = str(pqr)
            y.append(pqr)

    for figure in soup.findAll('figure', {'class': 'story-img'}):
        for a in figure('a'):
            for img in a('img', {'class': 'img-full'}):
                source = img.get('src')
                source = str(source)
                z.append(source)

    for i in range(len(x)):
        mt.append([x[i], y[i], z[i]])

    con = mdb.connect('localhost', 'root', 'adityagupta', 'cricket')
    with con:
        cur = con.cursor()
        cur.execute(
            "CREATE TABLE IF NOT EXISTS news(Id INT PRIMARY KEY AUTO_INCREMENT, Title VARCHAR(100),Story VARCHAR(500),Image VARCHAR(200))")
        for a in mt:
            cur.execute(
                "INSERT INTO news(Title,Story,Image) values (%s,%s,%s)", (a[0], a[1], a[2]))

    print '\n\nData Fetched!!\n'


if __name__ == '__main__':
    con = mdb.connect('localhost', 'root', 'adityagupta', 'cricket')
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS news")
    news()
