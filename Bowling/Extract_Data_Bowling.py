import requests
from tabulate import tabulate
from bs4 import BeautifulSoup
import sys
from math import ceil


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

    # print tabulate(mat,tablefmt="fancy_grid").encode("utf8")

    print '\n\nExtraction Complete!!\n'


def player_stats(player, i ):

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
    fo = open("bowling_file.txt" , "a")
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

    # fo.write (tabulate(mt,tablefmt="fancy_grid").encode("utf8"))
    display(mt)
    

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
    
    with open("Bowling_data/match_%s" % ''.join(rand) , "r") as input_file:
        plain_text = input_file.read()

    soup = BeautifulSoup(plain_text, "lxml")
    for link in soup.findAll('div', {'class': 'innings-requirement'}):
        data = link.string
        return ' '.join(data.split())

def display(list):
    newlist.append(list)



def win_economy():
    economy = 0.0
    win = 0.0
    nr = 0.0
    lost = 0.0
    percentage = 0.0
    strng = 'India won'
    strng2 = 'No result'

    for stats in newlist:
        for name in stats:
            if name[12] == 'R Ashwin':
                # char = '-'
                economy = name[5]
                # if economy.find(char) > -1:
                #     economy = economy.replace("-", "")

                if economy != '-' :
                    if int(economy) <= 4.0:
                        res = name[11]
                        if res.find(strng) > -1:
                            win += 1
                        elif res.find(strng2) > -1:
                            nr +=1
                        else:
                            lost += 1

    percentage = (win*100/(win+lost))

    print 'Matches Won : ' + str(int(win)) 
    print 'Matches Lost : ' + str(int(lost))
    print 'No Result : ' + str(int(nr))
    print 'Win Percentage : %.2f ' % (ceil(percentage))


def win_runs():
    runs = 0
    win = 0.0
    nr = 0.0
    lost = 0.0
    percentage = 0.0
    strng = 'India won'
    strng2 = 'No result'
    
    for stats in newlist:
        for name in stats:
            if name[12] == 'Mohammed Shami':
                runs = name[2]
                if runs != '-':
                    if int(runs) <= 40  :
                        res = name[11]
                        if res.find(strng) > -1:
                            win += 1
                        elif res.find(strng2) > -1:
                            nr +=1
                        else:
                            lost += 1

    percentage = (win*100/(win+lost))

    print 'Matches Won : ' + str(int(win)) 
    print 'Matches Lost : ' + str(int(lost))
    print 'No Result : ' + str(int(nr))
    print 'Win Percentage : %.2f ' % (percentage)


def search(list,ground):
    for (i, v) in enumerate(list):
       if v == ground:
           return i
    return -1

def win_spinners():
    runs = 0
    win = 0.0
    nr = 0.0
    lost = 0.0
    percentage = 0.0
    strng = 'India won'
    strng2 = 'No result'
    odi_no = []
    
    for stats in newlist:
        for name in stats:
            if name[12] == 'R Ashwin':
              odi_no.append(name[9])

    print odi_no
            # if name[12] == 'RA Jadeja':


    # percentage = (win*100/(win+lost))

    # print 'Matches Won : ' + str(int(win)) 
    # print 'Matches Lost : ' + str(int(lost))
    # print 'No Result : ' + str(int(nr))
    # print 'Win Percentage : %.2f ' % (percentage)


if __name__ == '__main__':
    team()
    win_economy()
    win_runs()