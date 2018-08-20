import urllib 
from bs4 import BeautifulSoup
import urllib.request
import time
import wget
from datetime import datetime
from threading import Timer

x = datetime.today()
y = x.replace(day=x.day+1, hour=2, minute=0, second=0, microsecond=0)
delta_t=y-x

secs = delta_t.seconds+1

def getData():
    with open('companylist.txt') as f:
        content = f.readlines()

    for c in content:
        c = str(c)
        c = c.strip('\n')
        c = c.strip('\t')
        symbol = 'http://quotes.wsj.com/' + c + '/historical-prices/download?MOD_VIEW=page&num_rows=6299&range=6299&startDate=07/17/2014&endDate=07/17/2018'
        print(c)
        filename = '/Users/ianjamieson/desktop/ijvestments/companies/' + c + '.csv'
        urllib.request.urlretrieve(symbol, filename)

t = Timer(secs, getData)
t.start()
