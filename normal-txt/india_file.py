import requests
from tabulate import tabulate
from bs4 import BeautifulSoup


def team():
    url = 'http://stats.espncricinfo.com/ci/engine/stats/index.html?class=2;home_or_away=1;home_or_away=2;home_or_away=3;result=1;result=2;result=3;result=5;spanmax1=25+Aug+2015;spanmin1=25+Aug+2011;spanval1=span;team=6;template=results;type=batting'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "lxml")
    fo = open("India_file.txt", "w")
    mat = [[u'Player', u'Span', u'Mat', u'Inns', u'NO', u'Runs', u'HS',
            u'Ave', u'BF', u'SR', u'100', u'50', u'0', u'4s', u'6s']]
    for tr in soup.findAll('tr', {'class': 'data1'}):
        l = []
        for td in tr:
            fifty = td.string
            if fifty is not None and fifty != "\n":
                l.append(fifty)
        mat.append(l)

    fo.write(tabulate(mat, tablefmt="fancy_grid").encode("utf8"))

team()
