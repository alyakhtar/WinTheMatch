from bs4 import BeautifulSoup
import sys


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

    display(mt)


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


def display(list):
    newlist.append(list)


def win_count():
    runs = 0
    win = 0.0
    nr = 0.0
    lost = 0.0
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
                    if int(runs) >= 50 and int(runs) < 100:
                        res = name[13]
                        if res.find(strng) > -1:
                            win += 1
                        elif res.find(strng2) > -1:
                            nr += 1
                        else:
                            lost += 1

    percentage = (win*100/(win+lost))

    print 'Matches Won : ' + str(int(win))
    print 'Matches Lost : ' + str(int(lost))
    print 'No Result : ' + str(int(nr))
    print 'Win Percentage : %.2f ' % (percentage)


def win_location():
    win_home = 0.0
    nr_home = 0.0
    lost_home = 0.0
    win_away = 0.0
    nr_away = 0.0
    lost_away = 0.0
    percentage_home = 0.0
    percentage_away = 0.0
    strng = 'India won'
    strng2 = 'No result'
    grounds = ['Mumbai', 'Nagpur', 'Trivandrum', 'Lucknow', 'Srinagar', 'Chandigarh', 'Jaipur', 'Rajkot', 'Ahmedabad', 'Vadodara',
               'Hyderabad (Deccan)', 'Pune', 'Madras', 'Kochi', 'Indore', 'Guwahati', 'Margao', 'Faridabad', 'Jammu', 'Patna', 'Chennai', 'Bangalore', 'Jamshedpur', 'Ranchi', 'Delhi', 'Visakhapatnam', 'Vijayawada', 'Dharamsala', 'Kanpur', 'Jalandhar', 'Amritsar', 'Kolkata', 'Gwalior', 'Jodhpur', 'Cuttack']

    for stats in newlist:
        for ground in stats:
            if ground[14] == 'V Kohli':
                char = '*'
                runs = ground[0]
                if runs.find(char) > -1:
                    runs = runs.replace("*", "")

                if runs != 'DNB' and runs != 'TDNB':
                    if int(runs) >= 50 and int(runs) < 100:
                        flag = search(grounds, ground[9])
                        if flag >= 0:
                            res = ground[13]
                            if res.find(strng) > -1:
                                win_home += 1
                            elif res.find(strng2) > -1:
                                nr_home += 1
                            else:
                                lost_home += 1
                        else:
                            res = ground[13]
                            if res.find(strng) > -1:
                                win_away += 1
                            elif res.find(strng2) > -1:
                                nr_away += 1
                            else:
                                lost_away += 1

    percentage_home = (win_home*100/(win_home+lost_home))
    percentage_away = (win_away*100/(win_away+lost_away))

    print 'Matches Won at home : ' + str(int(win_home))
    print 'Matches Won away : ' + str(int(win_away))
    print 'Matches Lost at home : ' + str(int(lost_home))
    print 'Matches Lost away : ' + str(int(lost_away))
    print 'No Result at home : ' + str(int(nr_home))
    print 'No Result away : ' + str(int(nr_away))
    print 'Home Win Percentage : %.2f%%' % (percentage_home)
    print 'Away Win Percentage : %.2f%%' % (percentage_away)


def win_against():
    runs = 0
    win = 0.0
    nr = 0.0
    lost = 0.0
    percentage = 0.0
    strng = 'India won'
    strng2 = 'No result'

    for stats in newlist:
        for name in stats:
            if name[14] == 'V Kohli':
                if name[12] == 'Australia':
                    char = '*'
                    runs = name[0]
                    if runs.find(char) > -1:
                        runs = runs.replace("*", "")

                    if runs != 'DNB' and runs != 'TDNB':
                        if int(runs) >= 50 and int(runs) < 100:
                            res = name[13]
                            if res.find(strng) > -1:
                                win += 1
                            elif res.find(strng2) > -1:
                                nr += 1
                            else:
                                lost += 1

    percentage = (win*100/(win+lost))

    print 'Matches Won : ' + str(int(win))
    print 'Matches Lost : ' + str(int(lost))
    print 'No Result : ' + str(int(nr))
    print 'Win Percentage : %.2f%% ' % (percentage)


def win_combined():
    win_home = 0.0
    nr_home = 0.0
    lost_home = 0.0
    win_away = 0.0
    nr_away = 0.0
    lost_away = 0.0
    percentage_home = 0.0
    percentage_away = 0.0
    strng = 'India won'
    strng2 = 'No result'
    grounds = ['Mumbai', 'Nagpur', 'Trivandrum', 'Lucknow', 'Srinagar', 'Chandigarh', 'Jaipur', 'Rajkot', 'Ahmedabad', 'Vadodara',
               'Hyderabad (Deccan)', 'Pune', 'Madras', 'Kochi', 'Indore', 'Guwahati', 'Margao', 'Faridabad', 'Jammu', 'Patna', 'Chennai', 'Bangalore', 'Jamshedpur', 'Ranchi', 'Delhi', 'Visakhapatnam', 'Vijayawada', 'Dharamsala', 'Kanpur', 'Jalandhar', 'Amritsar', 'Kolkata', 'Gwalior', 'Jodhpur', 'Cuttack']

    for stats in newlist:
        for ground in stats:
            if ground[14] == 'V Kohli':
                if ground[12] == 'Australia':
                    char = '*'
                    runs = ground[0]
                    if runs.find(char) > -1:
                        runs = runs.replace("*", "")

                    if runs != 'DNB' and runs != 'TDNB':
                        if int(runs) >= 50 and int(runs) < 100:
                            flag = search(grounds, ground[9])
                            if flag >= 0:
                                res = ground[13]
                                if res.find(strng) > -1:
                                    win_home += 1
                                elif res.find(strng2) > -1:
                                    nr_home += 1
                                else:
                                    lost_home += 1
                            else:
                                res = ground[13]
                                if res.find(strng) > -1:
                                    win_away += 1
                                elif res.find(strng2) > -1:
                                    nr_away += 1
                                else:
                                    lost_away += 1

    percentage_home = (win_home*100/(win_home+lost_home))
    percentage_away = (win_away*100/(win_away+lost_away))

    print 'Matches Won at home : ' + str(int(win_home))
    print 'Matches Won away : ' + str(int(win_away))
    print 'Matches Lost at home : ' + str(int(lost_home))
    print 'Matches Lost away : ' + str(int(lost_away))
    print 'No Result at home : ' + str(int(nr_home))
    print 'No Result away : ' + str(int(nr_away))
    print 'Home Win Percentage : %.2f%%' % (percentage_home)
    print 'Away Win Percentage : %.2f%%' % (percentage_away)


def search(list, ground):
    for (i, v) in enumerate(list):
        if v == ground:
            return i
    return -1


if __name__ == '__main__':
    team()
    print '\n***GENERAL CASE***\n'
    win_count()
    print '\n***HOME OR AWAY CASE***\n'
    win_location()
    print '\n***VERSUS CASE***\n'
    print '\nOPPONENT - AUSTRALIA\n'
    win_against()
    print '\n***COMBINED CASE***\n'
    win_combined()
