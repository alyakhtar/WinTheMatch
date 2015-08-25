import requests
from bs4 import BeautifulSoup

def team():
  url = 'http://stats.espncricinfo.com/ci/engine/stats/index.html?class=2;home_or_away=1;home_or_away=2;home_or_away=3;result=1;result=2;result=3;result=5;spanmax1=25+Aug+2015;spanmin1=25+Aug+2011;spanval1=span;team=6;template=results;type=batting'
  source_code = requests.get(url)
  plain_text = source_code.text
  soup = BeautifulSoup(plain_text,"lxml")  
  fo = open("newfile.txt" , "wb") 
  for link in soup.findAll('tr',{'class':'data1'}):
    for link2 in link('td'):
      fifty = link2.string
      if fifty is not None:
        fo.write(fifty.encode("utf8")+"\t")
    fo.write("\n")

team()