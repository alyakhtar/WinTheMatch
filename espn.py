import requests
from bs4 import BeautifulSoup


def player():
    global fo
    fo = open("players.txt", "wb")
    for i in xrange(1, 9):
        url = 'http://stats.espncricinfo.com/ci/engine/records/averages/batting.html?class=2;current=4;id=' + \
            str(i)+';type=team'
        team(url)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "lxml")
        for link in soup.findAll('tr', {'class': 'data1'}):
            for link2 in link('td', {'nowrap': 'nowrap'}):
                fifty = link2.string
                fo.write(fifty.encode("utf-8")+"\t")
            fo.write("\n")
        fo.write("\n\n")


def team(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "lxml")
    for link in soup.findAll('h1', {'class': 'SubnavSitesection'}):
        data = link.get_text()
    name = data.split('/')
    print name[1]
    fo.write(name[1].encode("utf-8")+"\n\n")
    # print name[13:24]


if __name__ == "__main__":
    player()
