import csv
import requests
from tabulate import tabulate
from bs4 import BeautifulSoup
import pandas as pd

def team():
  url = 'http://stats.espncricinfo.com/ci/engine/stats/index.html?class=2;home_or_away=1;home_or_away=2;home_or_away=3;result=1;result=2;result=3;result=5;spanmax1=25+Aug+2015;spanmin1=25+Aug+2011;spanval1=span;team=6;template=results;type=batting'
  source_code = requests.get(url)
  plain_text = source_code.text
  soup = BeautifulSoup(plain_text,"lxml")  
  fo = open("India_file.txt" , "w") 
  # mat = [[u'\n', u'Player', u'\n', u'Span', u'\n', u'Mat', u'\n', u'Inns', u'\n', u'NO', u'\n', u'Runs', u'\n', u'HS', u'\n', u'Ave', u'\n', u'BF', u'\n', u'SR', u'\n', u'100', u'\n', u'50', u'\n', u'0', u'\n', u'4s', u'\n', u'6s', u'\n', u'\n']]
  mat = [[u'Player',u'Span',u'Mat',u'Inns',u'NO',u'Runs',u'HS',u'Ave',u'BF',u'SR',u'100',u'50',u'0',u'4s',u'6s']]
  for tr in soup.findAll('tr',{'class':'data1'}):
    l = []
    for td in tr: 
      fifty = td.string
      if fifty is not None and fifty != "\n":
        l.append(fifty)
    mat.append(l)

  fo.write(tabulate(mat,tablefmt="fancy_grid").encode("utf8"))
  with open('India_csv.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(mat)
  df = pd.DataFrame(mat)
  df.to_csv("India_pandas.csv")
team()


