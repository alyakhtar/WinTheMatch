import requests
from bs4 import BeautifulSoup
import sys
import MySQLdb as mdb
from warnings import filterwarnings

filterwarnings('ignore', category=mdb.Warning)


def team():

    print 'Working...please wait\n'

    with open("Bowling_data/India.html", "r") as input_file:
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

    category = player_profile(player)
    catg = []
    catg.append(category)

    with open("Bowling_data/stats_%s" % player, "r") as input_file:
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
        mt[x].append(catg[0])

    con = mdb.connect('localhost', 'root', 'adityagupta', 'cricket')
    with con:
        cur = con.cursor()
        cur.execute(
            "CREATE TABLE IF NOT EXISTS bowling_statistics(Id INT PRIMARY KEY AUTO_INCREMENT, Overs VARCHAR(25) , Maidens VARCHAR(25), Runs VARCHAR(25), Wickets VARCHAR(25), Eco VARCHAR(25), Pos VARCHAR(25), Inns VARCHAR(25), Ground VARCHAR(40), Start_Date VARCHAR(25), ODI_NO VARCHAR(25), Opposition VARCHAR(30), Result VARCHAR(140), Player VARCHAR(30), Type VARCHAR(30))")

        for row in mt:
            cur.execute("""INSERT INTO bowling_statistics (Overs,Maidens,Runs,Wickets,Eco,Pos,Inns,Ground,Start_Date,ODI_NO,Opposition,Result,Player,Type) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (row[
                        0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13]))


def player_name(url, i):

    with open("Bowling_data/stats_%s" % url, "r") as input_file:
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

    with open("Bowling_data/match_%s" % ''.join(rand), "r") as input_file:
        plain_text = input_file.read()

    soup = BeautifulSoup(plain_text, "lxml")
    for link in soup.findAll('div', {'class': 'innings-requirement'}):
        data = link.string
        return ' '.join(data.split())


def player_profile(player):
    st = ''
    with open("Bowling_data/player_%s" % player, "r") as input_file:
        plain_text = input_file.read()

    soup = BeautifulSoup(plain_text, "lxml")
    for p in soup.findAll('p', {'class': 'ciPlayerinformationtxt'}):
        for span in p:
            abc = span.string
            if abc is not None:
                st += abc
    catg = player_style(st)
    return catg


def player_style(prof):
    spin_styles = ['offbreak', 'legbreak', 'orthodox']
    seam_styles = ['fast', 'medium']
    cat = '-'
    wow = prof.split()
    for style in wow:
        val = search(spin_styles, style.lower())
        if val > -1:
            cat = 'Spinner'
            break
        else:
            val2 = search(seam_styles, style.lower())
            if val2 > -1:
                cat = 'Seamer'
                break
    return cat


def search(list, style):
    for v in list:
        if style.find(v) > -1:
            return 1
    return -1


if __name__ == '__main__':
    con = mdb.connect('localhost', 'root', 'adityagupta', 'cricket')
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS bowling_statistics")
    team()
