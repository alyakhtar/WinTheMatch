from bs4 import BeautifulSoup
import MySQLdb as mdb
import sys, glob, os
from warnings import filterwarnings

filterwarnings('ignore', category = mdb.Warning)


def team():

    print 'Working...please wait\n'

    with open("Batting_data/India.html", "r") as input_file:
        plain_text = input_file.read()

    soup = BeautifulSoup(plain_text, "lxml")
    mat = []
    global newlist
    newlist = []
    i = 0
    global done
    done = 0
    for tr in soup.findAll('tr', {'class': 'data1'}):
        l = []
        if done == 46:
            i = 98
        for td in tr('td'):
            for a in td('a', {'class': 'data-link'}):
                abc = a.get('href')
                name = abc.split('/')
                player_stats(name[4], i)
            fifty = td.string
            if fifty is not None and fifty != "\n":
                l.append(fifty)
        i += 2.08
        done += 1
        mat.append(l)

    print '\n\nExtraction Complete!!\n'


def player_stats(player, i):

    with open("Batting_data/stats_%s" % player, "r") as input_file:
        plain_text = input_file.read()

    play = player_name(player, i)
    ply = []
    ply.append(play)

    soup = BeautifulSoup(plain_text, "lxml")

    global mt
    mt = []
    res = []
    opp = []

    for tr in soup.findAll('tr', {'class': 'data1'}):
        stat = []
        for td in tr('td'):
            for a in td('a', {'class': 'data-link'}):
                str1 = '/ci/content/team/'
                pqr = a.get('href')
                if pqr.find(str1) > -1:
                    pol = a.string
                    opp.append(' '.join(pol.split()))
            for a in td('a', {'title': 'view the scorecard for this row'}):
                xyz = a.get('href')
                lol = match_result(xyz)
                res.append(lol)
            dt = td.string
            if dt is not None and dt != "\n":
                stat.append(dt)
        mt.append(stat)

    mt.pop(0)
    mt.pop(0)
    for x in xrange(len(res)):
        mt[x].append(opp[x])
        mt[x].append(res[x])
        mt[x].append(ply[0])


    con = mdb.connect('localhost', 'root', 'samuraii', 'cricket')
    with con:
        cur = con.cursor()
        # cur.execute("DROP TABLE IF EXISTS statistics")
        cur.execute("CREATE TABLE IF NOT EXISTS statistics(Id INT PRIMARY KEY AUTO_INCREMENT, Runs VARCHAR(25) , Mins VARCHAR(25), BF VARCHAR(25), 4s VARCHAR(25), 6s VARCHAR(25), SR VARCHAR(25), POS VARCHAR(25), Dismissal VARCHAR(25), Inns VARCHAR(25), Ground VARCHAR(25), Start_Date VARCHAR(25), ODI_NO VARCHAR(25), Opposition VARCHAR(25), Result VARCHAR(150), Player VARCHAR(30))")

        for row in mt:
            cur.execute("""INSERT INTO statistics (Runs,Mins,BF,4s,6s,SR,POS,Dismissal,Inns,Ground,Start_Date,ODI_NO,Opposition,Result,Player) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]))



def player_name(url, i):

    with open("Batting_data/stats_%s" % url, "r") as input_file:
        plain_text = input_file.read()

    soup = BeautifulSoup(plain_text, "lxml")
    for link in soup.findAll('h1', {'class': 'SubnavSitesection'}):
        data = link.get_text()
    name = data.split('/')
    sys.stdout.write("\r[%s%s] %d%% Completed" %
                     ('=' * done, ' ' * (47-done), i))
    sys.stdout.flush()
    return ' '.join(name[2].split())


def match_result(url):
    rand = url.split("/")

    with open("Batting_data/match_%s" % ''.join(rand), "r") as input_file:
        plain_text = input_file.read()

    soup = BeautifulSoup(plain_text, "lxml")
    for link in soup.findAll('div', {'class': 'innings-requirement'}):
        data = link.string
        return ' '.join(data.split())