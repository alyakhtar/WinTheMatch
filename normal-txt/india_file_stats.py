import requests
from tabulate import tabulate
from bs4 import BeautifulSoup
import csv
import sys
import pandas as pd


def team():
    url = 'http://stats.espncricinfo.com/ci/engine/stats/index.html?class=2;home_or_away=1;home_or_away=2;home_or_away=3;result=1;result=2;result=3;result=5;spanmax1=25+Aug+2015;spanmin1=25+Aug+2011;spanval1=span;team=6;template=results;type=batting'
    print 'Fetching data...please wait\n'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "lxml")
    global fo
    fo = open("India_file_test.txt", "w")
    mat = [[u'Player', u'Span', u'Mat', u'Inns', u'NO', u'Runs', u'HS',
            u'Ave', u'BF', u'SR', u'100', u'50', u'0', u'4s', u'6s']]
    m = []
    i = 0
    global done
    done = 0
    for tr in soup.findAll('tr', {'class': 'data1'}):
        l = []
        if done == 46:
            i = 100
        for td in tr('td'):
            for a in td('a', {'class': 'data-link'}):
                abc = a.get('href')
                name = abc.split('/')
                # print name[4]
                player_stats(name[4], i)
                # m.append(abc)
            fifty = td.string
            if fifty is not None and fifty != "\n":
                l.append(fifty)
        i += 2.08
        done += 1
        mat.append(l)
    print '\nSearch Completed!!'
    # print tabulate(mat)
    # fo.write(tabulate(mat,tablefmt="fancy_grid").encode("utf8"))


def player_stats(player, i):
    stats = 'http://stats.espncricinfo.com/ci/engine/player/'+player + \
        '?class=2;home_or_away=1;home_or_away=2;home_or_away=3;result=1;result=2;result=3;result=5;spanmax1=25+Aug+2015;spanmin1=25+Aug+2011;spanval1=span;team=6;template=results;type=batting;view=innings'
    player_name(stats, i)
    source_code = requests.get(stats)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "lxml")
    mt = [[u'Runs', u'Mins', u'BF', u'4s', u'6s', u'SR', u'Pos',
           u'Dismissal', u'Inns', u'Ground', u'Start Date', u'ODI NO.']]
    res = [u'Result']
    opp = [u'Opposition']
    for tr in soup.findAll('tr', {'class': 'data1'}):
        stat = []
        for td in tr('td'):
            for a in td('a', {'class': 'data-link'}):
                str1 = '/ci/content/team/'
                pqr = a.get('href')
                if pqr.find(str1) > -1:
                    pol = a.string
                    opp.append(pol)
            for a in td('a', {'title': 'view the scorecard for this row'}):
                xyz = a.get('href')
                lol = match_result(xyz)
                res.append(lol)
            dt = td.string
            if dt is not None and dt != "\n":
                stat.append(dt)
        mt.append(stat)

    mt.pop(1)
    mt.pop(1)
    for x in xrange(len(res)):
        mt[x].append(opp[x])
        mt[x].append(res[x])
    fo.write(tabulate(mt, tablefmt="fancy_grid").encode("utf8"))


def player_name(url, i):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "lxml")
    for link in soup.findAll('h1', {'class': 'SubnavSitesection'}):
        data = link.get_text()
    name = data.split('/')
    sys.stdout.write("\r[%s%s] %d%% Completed" %
                     ('=' * done, ' ' * (47-done), i))
    # sys.stdout.write("\r%d%%\n Completed" % i)
    # print str(i)+"% Completed\n"
    fo.write("\n"+name[2]+"\n")


def match_result(url):
    result = 'http://www.espncricinfo.com'+url
    source_code = requests.get(result)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "lxml")
    for link in soup.findAll('div', {'class': 'innings-requirement'}):
        data = link.string
        return data
        # print data

team()
