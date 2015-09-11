import requests
from tabulate import tabulate
from bs4 import BeautifulSoup
import sys
import MySQLdb as mdb
from warnings import filterwarnings
# import MySQLdb as Database

filterwarnings('ignore', category = mdb.Warning)


def team():
    url = 'http://stats.espncricinfo.com/ci/engine/stats/index.html?class=2;home_or_away=1;home_or_away=2;home_or_away=3;result=1;result=2;result=3;result=5;spanmax1=25+Aug+2015;spanmin1=25+Aug+2011;spanval1=span;team=6;template=results;type=batting'
    print 'Working...please wait\n'
    source_code = requests.get(url)


    plain_text = source_code.text

    with open("html/india.html", "r") as input_file:
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


def player_stats(player, i ):

    with open("html/stats_%s" % player, "r") as input_file:
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

    display(mt)
    

def player_name(url, i):

    with open("html/stats_%s" % url, "r") as input_file:
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
    
    with open("html2/match_%s" % ''.join(rand) , "r") as input_file:
        plain_text = input_file.read()

    soup = BeautifulSoup(plain_text, "lxml")
    for link in soup.findAll('div', {'class': 'innings-requirement'}):
        data = link.string
        return ' '.join(data.split())

def display(list):
    newlist.append(list)

def win_count():
    runs = 0
    win = 0
    nr = 0
    lost = 0
    percentage = 0.0
    strng = 'India won'
    strng2 = 'No result'
    for stats in newlist:
        for name in stats:
            if name[14] == 'V Kohli':
                char = '*'
                runs = name[0]
                if runs.find(char) > -1:
                    runs = runs.replace("*", "")

                if runs != 'DNB' and runs != 'TDNB':
                    if int(runs) >= 50 and int(runs) <100 :
                        res = name[13]
                        if res.find(strng) > -1:
                            win += 1
                        elif res.find(strng2) > -1:
                            nr +=1
                        else:
                            lost += 1

    percentage = (win*100/(win+lost))

    print 'Matches Won : ' + str(win) 
    print 'Matches Lost : ' + str(lost)
    print 'No Result : ' + str(nr)
    print 'Win Percentage : %.2f ' % (percentage)



if __name__ == '__main__':
    team()
    win_count()