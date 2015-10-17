import requests
import sys
from bs4 import BeautifulSoup


def team():
    url = 'http://stats.espncricinfo.com/ci/engine/stats/index.html?class=2;home_or_away=1;home_or_away=2;home_or_away=3;result=1;result=2;result=3;result=5;spanmax1=25+Aug+2015;spanmin1=25+Aug+2011;spanval1=span;team=6;template=results;type=bowling'

    print 'Fetching data...please wait\n'

    source_code = requests.get(url)

    plain_text = source_code.text

    with open("Bowling_data/India.html", "w") as output_file:
        output_file.write(plain_text)

    done = 0
    i = 0

    soup = BeautifulSoup(plain_text, "lxml")
    for tr in soup.findAll('tr', {'class': 'data1'}):
        if done == 46:
            i = 98
        for td in tr('td'):
            for a in td('a', {'class': 'data-link'}):
                abc = a.get('href')
                name = abc.split('/')
                sys.stdout.write(
                    "\r[%s%s] %d%% Completed" % ('=' * done, ' ' * (47-done), i))
                sys.stdout.flush()
                player_stats(name[4])
        i += 2.08
        done += 1

    print '\n\nData Fetched!!\n'


def player_stats(player):
    player_profile(player)

    stats = 'http://stats.espncricinfo.com/ci/engine/player/'+player + \
        '?class=2;home_or_away=1;home_or_away=2;home_or_away=3;result=1;result=2;result=3;result=5;spanmax1=25+Aug+2015;spanmin1=25+Aug+2011;spanval1=span;team=6;template=results;type=bowling;view=innings'

    source_code = requests.get(stats)

    plain_text = source_code.text

    with open("Bowling_data/stats_%s" % player, "w") as output_file:
        output_file.write(plain_text)

    soup = BeautifulSoup(plain_text, "lxml")

    for tr in soup.findAll('tr', {'class': 'data1'}):
        for td in tr('td'):
            for a in td('a', {'title': 'view the scorecard for this row'}):
                xyz = a.get('href')
                match_result(xyz)


def match_result(url):

    result = 'http://www.espncricinfo.com'+url

    source_code = requests.get(result)

    rand = url.split("/")

    plain_text = source_code.text

    with open("Bowling_data/match_%s" % ''.join(rand), "w") as output_file:
        output_file.write(plain_text.encode("utf-8"))


def player_profile(player):
    player_link = 'http://www.espncricinfo.com/ci/content/player/'+player

    source_code = requests.get(player_link)

    plain_text = source_code.text

    with open("Bowling_data/player_%s" % player, "w") as output_file:
        output_file.write(plain_text.encode("utf-8"))

if __name__ == "__main__":
    team()
