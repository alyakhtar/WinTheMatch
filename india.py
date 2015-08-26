import csv
import requests
from tabulate import tabulate
from bs4 import BeautifulSoup

def team():
  url = 'http://stats.espncricinfo.com/ci/engine/stats/index.html?class=2;home_or_away=1;home_or_away=2;home_or_away=3;result=1;result=2;result=3;result=5;spanmax1=25+Aug+2015;spanmin1=25+Aug+2011;spanval1=span;team=6;template=results;type=batting'
  source_code = requests.get(url)
  plain_text = source_code.text
  soup = BeautifulSoup(plain_text,"lxml")  
  fo = open("newfile.txt" , "w") 
  mat = [[u'\n', u'Player', u'\n', u'Span', u'\n', u'Mat', u'\n', u'Inns', u'\n', u'NO', u'\n', u'Runs', u'\n', u'HS', u'\n', u'Ave', u'\n', u'BF', u'\n', u'SR', u'\n', u'100', u'\n', u'50', u'\n', u'0', u'\n', u'4s', u'\n', u'6s', u'\n', u'\n']]
  for tr in soup.findAll('tr',{'class':'data1'}):
    l = []
    for td in tr: 
      fifty = td.string
      if fifty is not None:
        l.append(fifty)
    mat.append(l)

  q = []
  for i in mat:
    r = []
    for x in i:
      if x != "\n":
        r.append(x)
    q.append(r)

  fo.write(tabulate(q,tablefmt="fancy_grid").encode("utf8"))
  with open('newfile.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(q)
team()


